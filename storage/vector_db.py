import chromadb
from sentence_transformers import SentenceTransformer
import openai


input_objective = "Get me a list of CPOs from USA "
objectives_file_path = "storage/objectives.txt"
task_lists_file_path = "storage/task_lists.txt"
db_path = "storage/vec_db"
collection_name = "objectives"

def get_openai_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    response = openai.Embedding.create(input=[text], model=model)
    return response['data'][0]['embedding']

def get_sentence_transformer_embedding(text, model_name='multi-qa-MiniLM-L6-cos-v1'):
    model = SentenceTransformer(model_name)
    return model.encode([text])[0].tolist()


class CustomEmbeddingFunction:
    def __init__(self, method='openai', model_name='text-embedding-ada-002'):
        self.method = method
        self.model_name = model_name
        if method == 'sentence_transformer':
            self.model = SentenceTransformer(model_name)

    def __call__(self, input):
        if self.method == 'openai':
            return get_openai_embedding(input, self.model_name)
        elif self.method == 'sentence_transformer':
            return self.model.encode([input])[0].tolist()


def read_data(objectives_file_path, task_lists_file_path):
    # Read objectives and map them to keys
    key_to_objective = {}
    with open(objectives_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            key, objective = line.strip().split(':', 1)
            key_to_objective[key.strip()] = objective.strip()

    # Read task lists and map them to keys
    key_to_tasks = {}
    with open(task_lists_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            key, tasks = line.strip().split(':', 1)
            key_to_tasks[key.strip()] = tasks.strip()

    return key_to_objective, key_to_tasks


def initialize_and_search(input_objective, objectives_file_path="storage/objectives.txt", task_lists_file_path="storage/task_lists.txt", db_path="storage/vec_db", collection_name="objectives",top_k=1):
    # Initialize SentenceTransformer and Chroma Client
    embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    #custom_embedding_function = CustomEmbeddingFunction(embedding_model)
    custom_embedding_function = CustomEmbeddingFunction(method="openai")


    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_or_create_collection(name=collection_name, embedding_function=custom_embedding_function)

    key_to_objective, key_to_tasks = read_data(objectives_file_path, task_lists_file_path)

    if not collection.count():
        for key, objective in key_to_objective.items():
            collection.add(
                embeddings=[embedding_model.encode(objective).tolist()],
                metadatas=[{"ID": key}],
                documents=[objective],
                ids=[key]
            )

    query_vector = embedding_model.encode(input_objective).tolist()
    res = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        include=['documents'],
    )

    if res['documents']:
        # Process multiple documents
        closest_objectives = [doc for doc in res['documents'][0]]
        # Debugging information
        #print(f"Closest Objectives Found: {closest_objectives}")
        #print(f"Objectives in Dictionary: {list(key_to_objective.values())}")

        # Find matching task lists for each closest objective
        results = []
        for closest_objective in closest_objectives:
            matching_keys = [key for key, obj in key_to_objective.items() if obj == closest_objective]
            if matching_keys:
                objective_key = matching_keys[0]
                matching_task_list = key_to_tasks.get(objective_key, [])
                results.append((closest_objective, matching_task_list))
            else:
                results.append(("No exact match found in objectives", []))
        
        return results
    else:
        return [("No matches found", [])]



#results = initialize_and_search(input_objective,top_k=5)

# Iterate over the results
#for closest_objective, task_list in results:
    # Process each closest objective and its task list
#    print(f"Closest Objective: {closest_objective}")
#    print(f"Associated Task List: {task_list}")

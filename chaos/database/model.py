from .prompt import get_database_template
from langchain.agents import AgentType, initialize_agent, Tool, load_tools
from langchain.chat_models import ChatOpenAI
from pymongo import MongoClient

import json

class DatabaseAgent:
  def __init__(self, openai_api_key, connection, database, model="gpt-4-32k", temperature=0.75, verbose=True):
    self.openai_api_key = openai_api_key
    self.database = MongoClient(connection)[database]
    self.model = model
    self.temperature = temperature
    self.verbose = verbose

  def get_metadata(self, collection):
    def extract_keys(document, parent=None):
      keys = set()
      for key, value in document.items():
        if isinstance(value, dict):
          keys.update(extract_keys(value, key))
        else:
          if parent is None:
            keys.add((key, type(value)))
          else:
            keys.add((f"{parent}.{key}", type(value)))
      return keys
    keys = set()
    # fetch random 100 rows to get metadata
    for document in list(self.database[collection].aggregate([{"$sample": {"size": 100}}])):
      keys.update(extract_keys(document))
    return keys

  def reader(self, query):
    try:
      data = json.loads(query)
      collection = data["collection_name"]
      aggregation = data.get("aggregation", None)
      if aggregation is not None:
        return list(self.database[collection].aggregate(aggregation))
      query = data["query"]
      projection = data.get("projection", {})
      cursor = self.database[collection].find(query, projection)
      if "sort" in data:
        sort = [(k, v) for k, v in data["sort"].items()]
        if len(sort) > 0:
          cursor = cursor.sort(sort)
      if (limit := data.get("limit", -1)) > 0:
        cursor = cursor.limit(limit)
      return list(cursor)
    except Exception as e:
      return str(e)

  def run(self, objective, dependency_info=[]):
    dependency_output = ""
    if len(dependency_info) > 0:
      dependency_output += "\n".join(dependency_info)
    dependency_output = dependency_output[:20000]

    database_task_model = ChatOpenAI(temperature=self.temperature, model_name=self.model, openai_api_key=self.openai_api_key)
    tools = load_tools(["llm-math"], llm=database_task_model)
    tools.append(Tool(
      name="Mongo database metadata search",
      func=self.get_metadata,
      description="You can use this tool when you want to find metadata like the names of columns present in a MongoDB collection. the input should be a single word without any spaces"
    ))
    tools.append(Tool(
      name="Mongo database reader",
      func=self.reader,
      description="""
      You can use the tool when you want to read data from a MongoDB collection. 
      If the query is analytical like grouping by a certain field, counting the size or number of a certain field then make sure you use an aggregation.
      If the query is to perform simple reads then use a query and projection to indicate your query.
      the input should be in one of the following formats
      {{
        "collection_name": the name of the collection on which the query must run it must be a single word without any spaces,
        "query": a MongDB valid query,
        "projection": a valid projection of which columns have to be selected,
        "sort": a dictionary of {{field_name: sort_order}}, where the sort_order is 1 if its ascending else -1 only if present in the query else do not include this key,
        "limit": a number that represents the total number of rows to be selected only if present in the query else should be default to -1
      }}
      or 
      {{
        "collection_name": the name of the collection on which the query must run it must be a single word without any spaces,
        "aggregation": a list of MongoDB aggregation pipeline stages
      }}
      """
    ))

    agent = initialize_agent(
      tools, 
      database_task_model, 
      agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
      verbose=self.verbose,  
      handle_parsing_errors=True,
      max_iterations=15,
      max_execution_time=None,
      early_stopping_method="generate"
    )
    model_response = agent.run(get_database_template().format(question=objective))
    return model_response
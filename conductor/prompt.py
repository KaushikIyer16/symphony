from .examples import task_generation_examples
from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from textwrap import dedent


def get_prompt():
  # Define an example prompt template for task generation
  example_prompt = PromptTemplate(input_variables=["objective", "taskList"], template="OBJECTIVE:{objective}\n{taskList}")
  return FewShotPromptTemplate(
    examples=task_generation_examples, # Examples for few-shot learning
    example_prompt= example_prompt, # Example prompt template
    prefix=dedent("""
    You are an expert task creation AI tasked with creating a list of tasks as a JSON array, considering the ultimate objective of your team: 
    Create new tasks based on the objective. Limit tasks types to those that can be completed with the available tools listed below. Task description should be detailed.
    Task description should be questions and must be answered in English.
    Current tool options are [text-completion] [web-search] [scraping] [linkedin].
    For tasks using [web-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes'). Result will be a summary of relevant information from the first few articles.
    When requiring multiple searches, use the [web-search] multiple times. This tool will use the dependent task result to generate the search query if necessary.
    Tasks that require summarization, rephrasing or compilation should use [text-completion], provide it the entire text obtained from the dependent tasks.
    dependent_task_ids should always be an empty array, or an array of numbers representing the task ID it should pull results from.
    [scraping] tool should be used whenever we want to extract information from previous tasks or tasks that contain URLs.
    [linkedin] tool should be used when we want to find information about a certain person or company, the objective should be a valid linkedin URL
    Make sure all task IDs are in chronological order.
    """),
    suffix="OBJECTIVE:{objective}\nTASK LIST=",
    input_variables=["objective"]
  )
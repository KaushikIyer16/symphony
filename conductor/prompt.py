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

def get_new_prompt():
  return PromptTemplate(
    template = """
  You are an expert task creation AI tasked with creating a list of tasks as a JSON array, considering the ultimate objective of your team: 
Create new tasks based on the objective by breaking it down into simpler problems.

Rules:
- "Task" is the input given to the tool, it should match the input format specified on the tool.
- Limit tasks types to those that can be completed with the available tools listed below.
- Always verify the correct input formats for each tool.
- Use as many tools as you need, to get the most comprehensive output.
- A task can have multiple dependent tasks. Do not hesitate to create such tasks.
- Make sure all task IDs are in chronological order.
- The final task's output is the only one returned to the user. So ensure the final task takes care of this.


The task list you generate should be [ALWAYS] be of this format, a list of JSONs:


[
{{"thought": <str>,"input_verification_thought":<str>, "id": <number>,"task": <str> ,"tool":<str>,"dependent_task_ids":<list of numbers>,"status":<"complete","incomplete">,"result":null,"result_summary":null}},
{{"thought": <str>,"input_verification_thought":<str>, "id": <number>,"task": <str> ,"tool":<str>,"dependent_task_ids":<list of numbers>,"status":<"complete","incomplete">,"result":null,"result_summary":null}},
{{"thought": <str>,"input_verification_thought":<str>, "id": <number>,"task": <str> ,"tool":<str>,"dependent_task_ids":<list of numbers>,"status":<"complete","incomplete">,"result":null,"result_summary":null}},
........
]




Tools: [text-completion] [web-search] [scraping] [text-extractor]

[text-completion]
- Description: Tasks that require summarization, rephrasing or compilation should use this tool. Can also be used on texts obtained from dependent tasks.
- Input:  Body of Text to be summarized, rephrased or compiled (mention which objective)
- Output: Summarized/Rephrased/Compiled text.

[web-search-without-scrape]
- Description: Tasks that require the use of web search without any further scraping (shallow search) should use this tool. Use this tool multiple times if you need multiple search results. This tool will use the dependent task result to generate the search query if necessary.
- Input: Only the search query (eg. input should not be 'search for waterproof shoes', instead it should be 'waterproof shoes') 
- Output: Result will be a summary of relevant information from the first few articles' rich data from google.

[web-search-with-scrape] 
- Description: This tool should be used whenever we want to perform a deep search. Search the query first, and then get the top 10 URLs. Scrape those resulting URLs further and summarize the results. Use this tool multiple times if you need multiple search results. This tool will use the dependent task result to generate the search query if necessary.
- Input: Only the search query (eg. input should not be 'search for waterproof shoes', instead it should be 'waterproof shoes') 
- Output: Result will be a detailed summary of relevant information from the first few articles on google.

[text-extractor]
- Description: This tool should be used when we want to extract specific sections or topics from a body of text. This task should always have a dependency task. 
- Input: The name of the section/portion to be extracted from the dependency task.
- Output: The result will be a short paragraph with the relevant sections/topics extracted and summarized from the full text(dependancy task).

Let's work this out in a step by step way to be sure we have the right answer. 

{examples}

Objective: {objective}
TaskList: 
""", input_variables = ["objective","examples"]
  )
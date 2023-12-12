from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from textwrap import dedent


def get_prompt():
  return PromptTemplate(
    template = """
  You are an expert task evaluation Auditor. Given a tool list, Objective, and Task List, your role is to meticulously assess whether the task list can successfully achieve the objective and deliver your assessment.

Your reasoning process should be methodical and detailed, and the outcome should [ALWAYS] be presented in the following JSON format:

{{
  "auditor_thoughts": <str>,
  "evaluation_summary": <str>,
  "verdict": <str: "Pass" or "Fail">
}}



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

Objective: {objective}

TaskList: {task_list}
""", input_variables = ["objective","task_list"]
  )

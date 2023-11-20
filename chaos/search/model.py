from langchain import GoogleSearchAPIWrapper
from langchain.agents import AgentType, initialize_agent, Tool, load_tools
from langchain.chat_models import ChatOpenAI
from .prompt import get_search_executor_template

class SearchAgent:
  def __init__(self, openai_api_key, google_api_key, google_cse_id, model="gpt-4-32k", temperature=0.75, verbose=True):
    self.openai_api_key = openai_api_key
    self.google_api_key = google_api_key
    self.google_cse_id = google_cse_id
    self.model = model
    self.temperature = temperature
    self.verbose = verbose

  def run(self, objective, task, dependency_info):
    dependency_output = ""
    if len(dependency_info) > 0:
      dependency_output += "\n".join(dependency_info)
    dependency_output = dependency_output[:20000]

    search_task_model = ChatOpenAI(temperature=self.temperature, model_name=self.model, openai_api_key=self.openai_api_key)
    tools = load_tools(["llm-math", "wikipedia"], llm=search_task_model)
    google_search_api = GoogleSearchAPIWrapper(
      google_api_key = self.google_api_key,
      google_cse_id = self.google_cse_id
    )
    tools.append(Tool(
      name="Current Search",
      func=google_search_api.run,
      description="You can use this tool when you want to search some information to get information on topics that you may not know"
    ))

    agent = initialize_agent(
      tools, search_task_model, 
      agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
      verbose=self.verbose, 
      return_intermediate_steps=True, 
      handle_parsing_errors=True,
      max_iterations=15,
      max_execution_time=None,
      early_stopping_method="generate"
    )
    model_response = agent(
      {
        "input": get_search_executor_template().format(
          objective=objective, 
          task=task, 
          dependent_task_output=dependency_output
        )
      })
    return model_response["output"]
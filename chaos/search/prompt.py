from langchain import PromptTemplate

def get_search_executor_template():
  return PromptTemplate(
  template="""
  ### Complete Your Assigned Task Based on the Objective and Dependent Task Output ###

  Complete your assigned task based on the objective and based on information provided in the dependent task output, if provided.
  If no relevant dependent task output is provided then you can use the Google Search tool and the Wikipedia tool to obtain more information.
  Your objective: {objective}.
  Your task: {task}
  Dependent task output: {dependent_task_output}
  Let's think step by step and incorporate as many sources of information as possible
  Output=
  """, input_variables=["objective", "task", "dependent_task_output"])
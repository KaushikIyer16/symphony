from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from .prompt import *

import json

class Conductor:
  def __init__(self, openai_api_key, model_name="gpt-4", temperature=0.9, verbose=True) -> None:
    self.openai_api_key = openai_api_key
    self.model_name = model_name
    self.temperature = temperature
    self.verbose = verbose
  
  def run(self, objective):
    task_creator_model = ChatOpenAI(temperature=0.9,model_name=self.model_name, openai_api_key=self.openai_api_key)
    chain = LLMChain(llm=task_creator_model, prompt=get_prompt(), verbose=self.verbose)
    return json.loads(chain.run(objective=objective))
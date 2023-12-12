from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from .prompt import *

import ast

class Critic:
    def __init__(self, openai_api_key, model_name="gpt-4-32k", temperature=0.9, verbose=True) -> None:
        self.openai_api_key = openai_api_key
        self.model_name = model_name
        self.temperature = temperature
        self.verbose = verbose
        self.empirical_bias = "EMPIRICAL CERTAINTY and BREADTH OF SEARCH"
        self.efficiency_bias = "CRITICAL PATH and EFFICIENCY"

    def score(self, objective, candidate_task_lists, mode = "empirical"):
        scorer_model = ChatOpenAI(temperature=0.9,model_name=self.model_name, openai_api_key=self.openai_api_key)
        chain = LLMChain(llm=scorer_model, prompt=get_prompt(), verbose=self.verbose)
        selected_bias = self.empirical_bias 
        if mode == "efficiency":
            selected_bias = self.efficiency_bias
        return ast.literal_eval(chain.run(objective=objective, candidate_task_lists = candidate_task_lists, bias = selected_bias))
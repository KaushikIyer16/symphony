from .prompt import get_retriever_prompt
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from vector_store.base_store import BaseStore
from langchain.embeddings.openai import OpenAIEmbeddings

import json

class LimitlessRetriever:
  def __init__(self, vector_store: BaseStore, dimension_definition: str, model: ChatOpenAI, k: int = 10, verbose: bool = True, strict = False):
    self.vector_store = vector_store
    self.dimensions = dimension_definition
    self.count = k
    self.model = model
    self.verbose = verbose
    self.strict = strict
  
  def get_embedding(self):
    return OpenAIEmbeddings(
        openai_api_key="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"
    )

  def run(self, query):
    chain = LLMChain(llm=self.model, prompt=get_retriever_prompt(), verbose=self.verbose)
    dimension_spec = json.loads(chain.run(dimension=self.dimensions, query=query))
    count = dimension_spec.get("count", {"$eq": self.count})["$eq"]
    payload = {}
    _filter = {}
    for key, value in dimension_spec.items():
      if key != "count":
        if "$eq" in value.keys():
          payload[key] = value["$eq"]
          if self.strict:
            _filter[key] = value
        else:
          _filter[key] = value
    payload = {key: value for key, value in dimension_spec.items() if key != "count"}
    vector = self.get_embedding().embed_query(json.dumps(payload))
    return self.vector_store.find_top_x(vector=vector, x=count, namespace="weather", filter=_filter)
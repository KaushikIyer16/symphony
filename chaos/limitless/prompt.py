from langchain.prompts import PromptTemplate

def get_retriever_prompt():
  return PromptTemplate(template="""
  query: {query}

  Extract the components of the above query and convert it to the following JSON definition.
  Do not add any new keys. If data is not present do not include the key. respond with only the JSON:
  
  Each key in the definition has a name, type and an explanation on what the value must be.
  The type can be one of number, string and can contain nested values.
  each value in the definition should contain the following:
  - $eq if it is equal to and the type is number or string
  - $gt if it is greater than and the type is number
  - $gte if it is greater than equal to and the type is number
  - $lt if it is lesser than and the type is number
  - $lte if it is lesser than equal to and the type is number
  - $ne if it is not equal to and the type is number
  {dimension}
  """, input_variables=["query", "dimension"])
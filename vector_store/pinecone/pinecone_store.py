from vector_store.base_store import BaseStore

import pinecone

class PineconeStore(BaseStore):

  def __init__(self, credentials, pinecone_api_key, environment, index_name):
    super().__init__(credentials)
    self.pinecone_api_key = pinecone_api_key
    self.index_name = index_name
    pinecone.init(api_key=pinecone_api_key, environment=environment)
    self.index = pinecone.Index(index_name=index_name)
  
  def find_top_x(self, vector, x=10, **kwargs):
    namespace = kwargs.get("namespace", None)
    if namespace is not None:
      _filter = kwargs.get("filter", {})
      return self.index.query(namespace=namespace,vector=vector, top_k=x, include_metadata=True, filter=_filter)
    else:
      return self.index.query(vector=vector, top_k=x, include_metadata=True)
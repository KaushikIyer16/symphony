from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

import pinecone

pinecone_api_key = "eb35a84f-779f-441f-844f-db21bba98b4f"
environment = "us-east-1-aws"
index_name = "auto-gpt"
namespace = "sec"
pinecone.init(api_key=pinecone_api_key, environment=environment)

def get_embedding():
  return OpenAIEmbeddings(
      openai_api_key="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"
  )

def get_index(index_name):
  return pinecone.Index(index_name=index_name)

def get_langchain_retriever(index_name, namespace, text_key):
  return Pinecone(get_index(index_name), get_embedding().embed_query, text_key, namespace).as_retriever()

ask_qa_model = ChatOpenAI(temperature=0.75,model_name="gpt-4-32k", openai_api_key="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")
qa = RetrievalQA.from_chain_type(
    llm=ask_qa_model, 
    chain_type='stuff',
    retriever=get_langchain_retriever("auto-gpt", "sec","text"),
  )
print(qa.run("is there any info on common stock?"))
from trafilatura import extract
from playwright.sync_api import sync_playwright
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from uuid import uuid4

import pinecone

def get_embedding():
  return OpenAIEmbeddings(
      openai_api_key="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"
  )

def split_texts(large_text: str):
  text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=10, separator=" ")
  return text_splitter.split_text(large_text)

def add_to_pinecone(large_text):
  pinecone_api_key = "eb35a84f-779f-441f-844f-db21bba98b4f"
  environment = "us-east-1-aws"
  index_name = "auto-gpt"
  namespace = "sec"
  embedding = get_embedding()
  pinecone.init(api_key=pinecone_api_key, environment=environment)
  texts = split_texts(large_text)
  res = []
  for chunk_id, text in enumerate(texts):
    res.append({
        "id": str(uuid4()),
        "values": embedding.embed_query(text),
        "metadata": {
            "text": text,
            "chunk_id": chunk_id
        }
    })
  pinecone.Index(index_name).upsert(res, namespace=namespace)


with sync_playwright() as p:
  browser = p.chromium.launch()
  with browser.new_context(user_agent="Involve AI") as context:
    page = context.new_page()
    page.goto(url='https://www.sec.gov/Archives/edgar/data/1656634/000095017023061116/grts-20230930.htm')
    downloaded = page.content()
    result = extract(downloaded)
    add_to_pinecone(result)

# print(Page.inner_html())
# downloaded = fetch_url("https://www.sec.gov/ix?doc=/Archives/edgar/data/0001656634/000095017023061116/grts-20230930.htm")
# downloaded = fetch_url('https://www.sec.gov/Archives/edgar/data/1656634/000095017023061116/grts-20230930.htm')
# result = extract(downloaded)
# print(result)
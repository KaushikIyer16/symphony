import pinecone
import pandas as pd
import json
import uuid

from tqdm import tqdm
from geopy.geocoders import Nominatim
from langchain.embeddings.openai import OpenAIEmbeddings

# Pinecone credentials and index details
pinecone_api_key = "eb35a84f-779f-441f-844f-db21bba98b4f"
environment = "us-east-1-aws"
index_name = "auto-gpt"
namespace = "weather"

# Load CSV data into a Pandas DataFrame (replace 'your_csv_file.csv' with your actual CSV file)
csv_file_path = '~/Downloads/weather_data/main.csv'
df = pd.read_csv(csv_file_path)

# Function to convert point data to numerical vectors
def convert_point_to_vector(point):
    return point

def get_embedding():
    return OpenAIEmbeddings(
        openai_api_key="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"
    )

def extract_coordinates(point):
    coordinates = point.strip('POINT ()').split()
    latitude, longitude = map(float, coordinates)
    return latitude, longitude

# Define a function to add data to Pinecone index
def add_data_to_pinecone(data, index_name, namespace):
    pinecone.init(api_key=pinecone_api_key, environment=environment)
    # Convert the point column to numerical vectors
    data['location'] = data['Geo_Loc'].apply(extract_coordinates)
    cleaned_data = data.drop(columns=['Geo_Loc'])
    json_obj = json.loads(cleaned_data.to_json(orient="records"))
    embedding = get_embedding()
    res = []
    for obj in tqdm(json_obj):
      tmp_obj = obj
      tmp_obj["latitude"] = obj["location"][0]
      tmp_obj["longitude"] = obj["location"][1]
      del tmp_obj["location"]
      _str = json.dumps(tmp_obj)
      res.append({
        "id": str(uuid.uuid4()),
        "values": embedding.embed_query(_str),
        "metadata": tmp_obj
      })
      if len(res) >= 100:
        pinecone.Index("auto-gpt").upsert(res, namespace="weather")
        res = []
    
    # Extract vectors and upsert data to Pinecone index
    # records = [{'point': row['point'], 'vector': row['vector']} for _, row in data.iterrows()]
    # print(records)
    # pinecone.Index("auto-gpt").query(
    #     namespace=namespace,
    #     vector=embedding.embed_query(query_str),
    #     top_k=count,
    #     include_metadata=True)

# Add data to Pinecone index
add_data_to_pinecone(df, index_name, namespace)

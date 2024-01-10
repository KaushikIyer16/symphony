from conductor.model import Conductor
from orchestra.main import Orchestra
from registry import get_registry
from chaos.database import DatabaseAgent
from chaos.limitless import LimitlessRetriever
from langchain.chat_models import ChatOpenAI
from vector_store.pinecone import PineconeStore

import json

conductor = Conductor(openai_api_key="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")
objective = "I have 2 cauliflowers and 1 onion left, what can I cook?"
tasks = conductor.run(objective)

orchestra = Orchestra(registry=get_registry())
print(orchestra.run(objective, tasks))

# DatabaseAgent(
#   openai_api_key="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", 
#   connection="mongodb+srv://mel:07M0MWpSLQW6GUYr@involve-ai-flask-prod-c.hmzys.mongodb.net/test?authSource=admin&replicaSet=atlas-ungnx4-shard-0&readPreference=primary&ssl=true",
#   database="r2d2"
#   ).run(
#     objective="what is the count of documents in leads that have a key called v2 and is set to true"
#   )

# simple_model = ChatOpenAI(
#   temperature=0.9, 
#   model_name="gpt-4-32k", 
#   max_retries=2,
#   openai_api_key="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")

# vector_store = PineconeStore(
#   credentials={}, 
#   pinecone_api_key="eb35a84f-779f-441f-844f-db21bba98b4f", 
#   environment="us-east-1-aws", 
#   index_name="auto-gpt")

# # dimension_definition = """
# # {{
# #   "title": "string", // job title if provided in the search
# #   "company_name": "string", // company names if provided in the search
# #   "location":
# #     {{
# #       "city": "string", // city names if provided in the search
# #       "state": "string", // state names if provided in the search
# #       "country": "string" // country names if provided in the search
# #     }},
# #   "industry": ["string"], // list of industries to be found if provided in the search
# #   "seniority": ["string"], // list of seniorities to be found and should be one of 'C suite', 'Director', 'Entry', 'Founder', 'Head', 'Intern', 'Manager', 'Owner', 'Partner', 'Senior', 'Vp', '', 'C-Suite', 'Consulting', 'Design', 'Education', 'Engineering & Technical', 'Finance', 'Human Resources', 'Information Technology', 'Legal', 'Marketing', 'Medical & Health', 'Operations', 'Sales'
# #   "departments": ["string"], // list of departments to be found if provided in the search,
# #   "no_of_employee": "string", //number of employee if present in the search              
# #   "count": "number" // number of leads to find
# # }}
# # """

# dimension_definition = """
# {{
#   "Good Days": number, // number of good days if provided in the query
#   "Year": number, // year if provided in the search
#   "latitude": number, // latitude of the location if provided in the query
#   "longitude": number, // longitude of the location if provided in the query
#   "State": string // state of the location if provided in the query
#   "count": number // number of results to be returned if provided in the query
# }}
# """

# retriever = LimitlessRetriever(
#   model=simple_model, 
#   dimension_definition=dimension_definition,
#   strict=True, 
#   vector_store=vector_store)

# print(retriever.run("200 years that have more than 1000 good days in New York after 2000"))
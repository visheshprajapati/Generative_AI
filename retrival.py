from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings , ChatOpenAI
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
import os

load_dotenv()

client = MongoClient("mongodb+srv://admin:admin@cluster0.kbxjhnq.mongodb.net/?appName=Cluster0")

db = client["LDRP_RAG"]
collection = db["documents"]

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)   

vector_store = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name="rag_index",
)

query = "What are the key skills mentioned in the cv?"

vector = vector_store.similarity_search(query = query, k=3)

context = " ".join(
    doc.page_content for doc in vector
)

prompt = f"""
Answer only based on the following context.

if Answer is not found in the context, say "I don't know".

Context: {context}
Question: {query}

"""

llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

response = llm.invoke(prompt)

print(response.content)
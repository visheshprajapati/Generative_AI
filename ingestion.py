from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

loader = PyPDFLoader("Vishesh_CV.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

client = MongoClient("mongodb+srv://admin:admin@cluster0.kbxjhnq.mongodb.net/?appName=Cluster0", tls=True)
db = client["LDRP_RAG"]
collection = db["documents"]

for doc in docs:
    embedding = embeddings.embed_query(doc.page_content)
    document_data = {
        "text": doc.page_content,
        "embedding": embedding
    }
    collection.insert_one(document_data)

print("Documents ingested and embeddings stored in MongoDB successfully.")
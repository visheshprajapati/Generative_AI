from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user","crate a question paper on topic {topic}.of marks {marks} and difficulty level {difficulty}")
    ]
)
chain = prompt | client
response = chain.stream(
    {
        "topic": "python programming",
        "marks": 100,
        "difficulty": "medium"
    }   
)
for chunk in response:
    print(chunk.content , end="", flush=True)
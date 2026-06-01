from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#this is the defualt and can be commited
#api_key = "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" 

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-3.5-turbo",
    instructions="Act as my helpful assistant",
    input="What is the capital of France",
)
print(response.output_text)
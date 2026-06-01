from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

import string

load_dotenv()

app = FastAPI()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

class QuestionPaperRequest(BaseModel):
    topic: str
    marks: int
    questiontype: str
    marksPerQuestion: int

@app.post("/generate-question-paper")
async def generate_question_paper(data: QuestionPaperRequest):

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a question paper generator."),
        ("user", "Create a question paper on {topic} of total marks {marks}, question type {questiontype}, with {marksPerQuestion} marks per question.")
    ])

    chain = prompt | client

    response = chain.invoke({
        "topic": data.topic,
        "marks": data.marks,
        "questiontype": data.questiontype,
        "marksPerQuestion": data.marksPerQuestion
    })

    return {
        "topic": data.topic,
        "questiontype": data.questiontype,
        "questionPaper": response.content
    }

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful assistant."),
#         ("user","crate a question paper on topic {topic}.of marks {marks} and difficulty level {difficulty}")
#     ]
# )
# chain = prompt | client
# response = chain.invoke(
#     {
#         "topic": "python programming",
#         "marks": 100,
#         "difficulty": "medium"
#     }   
# )
# print(response.content)
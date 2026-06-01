from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY")
)

class QuestionPaperBody(BaseModel):
    topic: str
    marks: int
    questiontype: str
    marksperquestion: int
    
class Question(BaseModel):
    question: str
    options: list[str]
    answer: str

class QuestionPaper(BaseModel):
    topic: str
    passing_marks: int
    question: list[Question]
    
parser = PydanticOutputParser(pydantic_object=QuestionPaper)

@app.post("/questionpaperGenerator")
def generate_question_paper(data: QuestionPaperBody):

    prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful question paper generator, {format}."),
                ("user", "Create a question paper on {topic} of marks {marks} and question type {questiontype} with {marksperquestion} marks per question."),
            ]
        )

    chain = prompt | client | parser

    response = chain.invoke({
            "topic": data.topic,
            "marks": data.marks,
            "questiontype": data.questiontype,
            "marksperquestion": data.marksperquestion,
            "format": parser.get_format_instructions()
        })

    print("\n=========== QUESTION PAPER ===========\n")
    print(response)
        
    return {
            "topic": data.topic,
            "questiontype": data.questiontype,
            "questionpaper": response.model_dump()
        }
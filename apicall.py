from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import requests
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    
    url = f'https://wttr.in/{city}?format=j1'
    response = requests.get(url)
    data = response.json()
    temp = data['current_condition'][0]['temp_C']
    
    return f"The current temperature in {city} is {temp}°C."


client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY")
)

client_with_tools = client.bind_tools([get_weather])

response = client_with_tools.invoke(
    "What is the current weather in Ahmedabad?"
)

print("\n=========== WEATHER ===========\n")
print(response.tool_calls)

if response.tool_calls:
    tool_call = response.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    result = get_weather.invoke(tool_args)

    print(result)
else:
    print(response.content)




# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.tools import tool
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # OpenAI Client
# client = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# # Tool
# @tool
# def get_weather(city: str) -> str:
#     """Returns weather information for a city."""

#     prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", "You are a weather assistant."),
#             ("user", "What is the weather like in {city}?")
#         ]
#     )

#     chain = prompt | client

#     response = chain.invoke({
#         "city": city
#     })

#     return response.content


# city_name = input("Enter city name: ")

# result = get_weather.invoke(city_name)

# print("\n========== WEATHER ==========\n")
# print(result)

# from pydantic import BaseModel
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import PydanticOutputParser
# from dotenv import load_dotenv
# import os

# load_dotenv()


# client = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     api_key = os.getenv("OPENAI_API_KEY")
# )   
    
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a weather assistant."),
#         ("user", "What is the weather like in {city}?")
#     ]
# )

# chain = prompt | client

# response = chain.invoke({
#     "city": input("Enter the city name: ")
# })

# print("\n=========== WEATHER ===========\n")
# print(response)
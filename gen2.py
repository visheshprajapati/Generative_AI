from openai import OpenAI

api_key = "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"
client = OpenAI(
    api_key=api_key
)       
message = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]
for i in range(3):
    user_input = input("User:")
    message.append({
        "role": "user",
        "content": user_input
    })
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    assistant_response = response.choices[0].message.content
    print("Assistant:", assistant_response)
    message.append({
        "role": "assistant",
        "content": assistant_response
    })




import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

x = enc.encode("Hello world")
print(x)

y = enc.decode(x)
print(y)

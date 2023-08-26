from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

result = llm("Write a poem.")
print(result)

token_count = llm.get_num_tokens("Why should you have the advantage over me?")
print(token_count)

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

result = llm.generate(["Write a poem about fire.", "Write a poem about water."])

print(result.generations[0][0].text)
print("\n")
print(result.llm_output)

from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

text = 'My favorite food is pizza.'

query_embedding = embeddings.embed_query(text)

print(query_embedding)

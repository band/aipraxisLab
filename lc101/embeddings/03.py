from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

text1 = 'My favorite food is pizza.'
text2 = 'My favorite food is tacos.'
text3 = 'My favorite food is ice cream.'

document_embeddings = embeddings.embed_documents([text1, text2, text3])

print(len(document_embeddings))

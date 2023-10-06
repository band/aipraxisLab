"""
2023-10-06: bare bones minimum
"""
# Define prompt
from langchain.prompts import PromptTemplate
prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""
prompt = PromptTemplate.from_template(prompt_template)

# Define LLM chain
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
from langchain.chains import LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Define StuffDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
stuff_chain = StuffDocumentsChain(
    llm_chain=llm_chain, document_variable_name="text"
)

from langchain.document_loaders import TextLoader
loader = TextLoader("./input.txt")
docs = loader.load()    

print(stuff_chain.run(docs))

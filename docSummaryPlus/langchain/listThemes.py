"""
2023-10-07: list themes; limited by token size of input text
"""
# Define prompt
from langchain.prompts import PromptTemplate
prompt_template = """List the primary themes of the following:
"{text}"
LIST OF THEMES:"""
prompt = PromptTemplate.from_template(prompt_template)

# Define LLM chain
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0.0, model_name="gpt-3.5-turbo-16k")
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

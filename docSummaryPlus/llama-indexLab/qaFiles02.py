#! /usr/bin/env python
"""
code derived from <https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5>
A step-by-step guide to building a chatbot based on your own documents with GPT

2023-03-18: only indexes Obsidian vaults
2023-08-05: a long way away from the first incarnation
"""

# Import the needed modules and items
from llama_index import VectorStoreIndex
from llama_index import download_loader
from llama_index.llms import OpenAI
from llama_index import ServiceContext

import os

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI index from directory of documents.')
    parser.add_argument('--directory', '-d', required=True, help='directory containing files (Markdown + other)')
    return parser

SimpleDirectoryReader = download_loader('SimpleDirectoryReader')
UnstructuredReader = download_loader('UnstructuredReader')

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    dir_name = str(args.directory)
    print(dir_name)

    # check API Key is set
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")
        sys.exit(1)

    # Load documents from a directory

    loader = SimpleDirectoryReader(dir_name, file_extractor={
        ".html": "UnstructuredReader",
        ".eml": "UnstructuredReader"})
    documents = loader.load_data() # returns list of documents

    model_name='gpt-3.5-turbo-16k'
    llm = OpenAI(model=model_name, temperature=0.0)
    service_context = ServiceContext.from_defaults(llm=llm)

    # Construct a simple vector index
    index = VectorStoreIndex(documents, service_context=service_context)

    # Save your index to a index.json file
#    index.save_to_disk('index.json')
    # Load the index from your saved index.json file
#    index = VectorStoreIndex.load_from_disk('index.json')

    # Querying the index
    query_engine = index.as_query_engine(
        service_context=service_context,
        response_mode="compact")
    
    response = query_engine.query("What are the social or economic concepts in the documents?")
    print("model: ", model_name)
    print(response)

if __name__ == "__main__":
    exit(main())


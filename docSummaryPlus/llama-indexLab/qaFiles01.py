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
SimpleDirectoryReader = download_loader('SimpleDirectoryReader')
UnstructuredReader = download_loader('UnstructuredReader')

import os

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI index from directory of documents.')
    parser.add_argument('--directory', '-d', required=True, help='directory containing files (Markdown + other)')
    return parser

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

    # Construct a simple vector index
    index = VectorStoreIndex(documents)

    # Save your index to a index.json file
#    index.save_to_disk('index.json')
    # Load the index from your saved index.json file
#    index = VectorStoreIndex.load_from_disk('index.json')

    # Querying the index
    query_engine = index.as_query_engine(
        response_mode="compact")
    
    response = query_engine.query("What are the primary concepts in the documents?")
    print(response)

if __name__ == "__main__":
    exit(main())


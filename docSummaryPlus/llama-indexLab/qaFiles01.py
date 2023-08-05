#! /usr/bin/env python
"""
code derived from <https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5>
A step-by-step guide to building a chatbot based on your own documents with GPT

2023-03-18: only indexes Obsidian vaults
2023-08-05: a long way away from the first incarnation
"""

# Import the needed modules and items
from llama_index import GPTSimpleVectorIndex, Document
from llama_index import download_loader
UnstructuredReader = download_loader('UnstructuredReader')
SimpleDirectoryReader = download_loader('SimpleDirectoryReader')

import os

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI index from directory of documents.')
    parser.add_argument('--directory', '-d', required=True, help='directory containing files (Markdown + other)')
    return parser

os.environ['OPENAI_API_KEY'] = ''

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    wiki_dir = str(args.directory)
    print(dir_name)

    # check API Key is set
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")
        sys.exit(1)

    # Load documents from a directory

    loader = SimpleDirectoryReader(wiki_name, file_extractor={
        ".html": "UnstructuredReader",
        ".eml": "UnstructuredReader"})
    documents = loader.load_data() # returns list of documents

    # Construct a simple vector index
    index = GPTSimpleVectorIndex(documents)

    # Save your index to a index.json file
    index.save_to_disk('index.json')
    # Load the index from your saved index.json file
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

    # Querying the index
    response = index.query("What are the primary concepts in the wiki pages?")
    print(response)

if __name__ == "__main__":
    exit(main())


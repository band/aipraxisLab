#! /usr/bin/env python
"""
code derived from <https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5>
A step-by-step guide to building a chatbot based on your own documents with GPT

2023-03-18: only indexes Obsidian vaults
"""

# Import necessary packages
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex
from llama_index import download_loader
import os

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI index from Massive Wiki Markdown pages.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    wiki_dir = str(args.wiki)
    print(wiki_dir)

    # Loading from a directory
#    documents = SimpleDirectoryReader(wiki_dir).load_data()

    ObsidianReader = download_loader('ObsidianReader')
    documents = ObsidianReader(wiki_dir).load_data() # Returns list of documents

    # Construct a simple vector index
    index = GPTVectorStoreIndex(documents)

    # Save your index to a index.json file
#    index.save_to_disk('index.json')
    # Load the index from your saved index.json file
#    index = GPTVectorStoreIndex.load_from_disk('index.json')

    # Querying the index
    query_engine = index.as_query_engine(
        response_mode="compact")
    
    response = query_engine.query("What are the primary concepts in the wiki pages?")
    print(response)

if __name__ == "__main__":
    exit(main())


#! /usr/bin/env python

# set up logging
import logging
#    - use INFO logging during developmentb
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
#    - use LOGLEVEL environment variable in deployment operation
# import os
# logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate summaryfrom a text or Markdown file.')
    parser.add_argument('--model', '-m', required=False, help='llm model_name')
    parser.add_argument('--filename', '-f', required=True, help='text or Markdown file name')
    return parser

# get HuggingFace pipeline transformer
from transformers import pipeline

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        return infile.read()

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")

    file_name = str(args.filename)
    logging.info("file name: %s", file_name)

    # define summarizer
    # use default 'summarization' model if none provided
    if args.model:
        model_name = str(args.model)
        logging.info("hf model name: %s", model_name)
        summarizer = pipeline(task="summarization", model=model_name)
    else:
        summarizer = pipeline(task="summarization")
    
    # read file
    logging.info("Reading from: %s ", file_name)
    text = read_file(file_name)

    summary = summarizer(text)

    print(summary)
    
if __name__ == "__main__":
    exit(main())


#! /usr/bin/env python
"""
Generate text summaries of a given input text using the Anthropic claude language model

Operating requirements:
  ANTHROPIC_API_KEY defined in the shell environment

This version of this program takes the following arguments:
1. '--file': the input text that is summarized
2. '--prompt': (optional) prompt text; if not specified a default 'list themes in this text' is used

"""
# set up logging
import logging, sys
# logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# get env info
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
anthropic = Anthropic()

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Use Anthropic claude-2 completion api to summarize specified document file')
    parser.add_argument('--file', '-f', required=True, help='file')
    parser.add_argument('--prompt', '-p', required=False, help='custom prompt text')
    return parser

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# prompt = f"{HUMAN_PROMPT} list key themes in this text: {text}{AI_PROMPT}"

def show_claude_completion(prompt):
    try:
        completion = anthropic.completions.create(model="claude-2",max_tokens_to_sample=32000,prompt=prompt)
        print(completion.completion)
    except Exception as err:
        print('Error communicating with Anthropic:', err)

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.info(f"args: {args}")
    
    file_name = str(args.file)
    logging.debug("document file : %s", file_name)

    text = read_file(file_name)
    prompt = f"{HUMAN_PROMPT} list key themes in this text and extract an illustrative quote for each theme: {text}{AI_PROMPT}"

#    if args.prompt:
#        prompt_text = read_file(args.prompt)

    show_claude_completion(prompt)

if __name__ == '__main__':
    exit(main())

#! /usr/bin/env python
"""
Generate text summaries of a given input text using an OpenAI language model by breaking the input into smaller chunks and generating a summary for each chunk using a GPT chat completion endpoint.

The summaries are then concatenated and saved to a file.

Operating requirements:
  OPENAI_API_KEY defined in the shell environment

This version of this program takes the following arguments:
1. '--file': the input text that is summarized
2. '--model': (optional) if not specified the gpt-3,.5-turbo model is used
3. '--prompt': (optional) prompt text; if not specified a simple 'summarize this text' is used

A concatenation of the individual text summaries is saved in the file 'output.txt'

"""
import openai
import os
import re

from langchain.text_splitter import RecursiveCharacterTextSplitter
#import textwrap

from time import time, sleep

# set up logging
import logging, sys
# logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Use OpenAI gpt ChatCompletion to summarize specified document file')
    parser.add_argument('--file', '-f', required=True, help='file')
    parser.add_argument('--model', '-m', required=False, help='LLM model name')
    parser.add_argument('--prompt', '-p', required=False, help='custom prompt text')
    return parser

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
        
def gpt_chat_completion(prompt, engine='gpt-4', temp=0.0, tokens=1800, top_p=0.1, freq_pen=0.25, pres_pen=0.0, stop=['<<END>>']):
    max_retry = 3
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(
                model=engine,
                messages=[{"role":"user", "content":prompt}],
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['message']['content']
#            text = re.sub('\s+', ' ', text)
            filename = '%s_gpt3or4.txt' % time()
            with open('gpt_logs/%s' % filename, 'w') as outfile:
                outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
            return text
        except Exception as err:
            retry += 1
            if retry >= max_retry:
                return f"{engine} error: %s" % err
            print('Error communucating with OpenAI:', err)
            sleep(1)


if __name__ == '__main__':
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.info(f"args: {args}")
    
    file_name = str(args.file)
    logging.debug("document file : %s", file_name)

    model_name = 'gpt-3.5-turbo'
    if args.model:
        model_name = str(args.model)

    prompt_text = ("Summarize the content chunk. Content: ```{chunk}```")
    if args.prompt:
        prompt_text = read_file(args.prompt)

    alltext = read_file(file_name)
    chunks = textwrap.wrap(alltext, 4096)
    result = list()
    for count, chunk in enumerate(chunks, 1):
        prompt = prompt_text.replace('{chunk}', chunk).encode(encoding='ASCII',errors='ignore').decode()
        summary = gpt_chat_completion(prompt, engine=model_name)
        print('\n\n\n', count, 'of', len(chunks), ' - ', summary)
        result.append(summary)
    save_file('\n\n'.join(result), 'output_%s.txt' % time())


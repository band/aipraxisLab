#! /usr/bin/env python
"""
This code generates text summaries of a given input text using the OpenAI GPT-3 language model by breaking it up into smaller chunks and generating a summary for each chunk using a GPT chat completion endpoint.

The summaries are then concatenated and saved to a file.

Operating requirements:
  OPENAI_API_KEY defined in the shell environment

This version of this program uses the following files:
1. input.txt [this file contains the text input of big file to summarize]
2. prompt.txt [this file contains how we want to summarize the text: the prompt used for GPT output]
3. output.txt [this file contains a concatenation of the prompt summaries]

"""
import openai
import os
import re
import textwrap
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
    return parser

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
        
def gpt_chat_completion(prompt, engine='gpt-4-0613', temp=0.0, tokens=1800, top_p=0.1, freq_pen=0.25, pres_pen=0.0, stop=['<<END>>']):
    max_retry = 5
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
            filename = '%s_gpt35.txt' % time()
            with open('gpt3_logs/%s' % filename, 'w') as outfile:
                outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3.5 error: %s" % oops
            print('Error communucating with OpenAI:', oops)
            sleep(1)


if __name__ == '__main__':
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")
    
    file_name = str(args.file)
    logging.info("document file : %s", file_name)

    alltext = open_file(file_name)
    chunks = textwrap.wrap(alltext, 1000)
    result = list()
    count = 0
    for chunk in chunks:
        count = count + 1
        prompt = open_file('prompt02.txt').replace('{chunk}', chunk)
        prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
        summary = gpt_chat_completion(prompt)
        print('\n\n\n', count, 'of', len(chunks), ' - ', summary)
        result.append(summary)
    save_file('\n\n'.join(result), 'output_%s.txt' % time())


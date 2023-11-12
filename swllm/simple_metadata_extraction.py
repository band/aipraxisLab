import openai
import os
from pathlib import Path
import subprocess

'''
TODO:
straighten out the file path naming
'''

# set up logging
import logging, sys
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper())
#logging.basicConfig(stream=sys.stdout, level=logging.INFO)
#logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Use an LLM to extract metadata from text files.')
    parser.add_argument('--directory', '-d', required=True, help='directory of text files')
#    parser.add_argument('--model', '-m', required=False, help='LLM model name')
    return parser

metadata_filename = ''
def run_command(mdfile, directory, filename):
    logging.info(f"{directory}/{filename}")
    command = f"cat {directory}/{filename} | ttok -t 4000 | llm --system 'create a json file from the contents of the text with the following keys: id, title, description, keywords. The id is {Path(filename).stem}. The description should be a 1-2 sentence summary of the text. The keywords are a list of no more than 5 terms.' >> {mdfile}"
    try:
        subprocess.run(command,shell=True,check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command for {filename}: {e}")

def main():

    args = init_argparse().parse_args();
    logging.info(f"args: {args}")

    directory = str(args.directory)
    mdfile = Path(directory).stem + '-metadata.json'
    logging.info(f"1 metadata_filename: {mdfile}")
    Path(mdfile).unlink(missing_ok=True)
    
    [run_command(mdfile, directory, f) for f in os.listdir(directory) if f.endswith('.txt')]

# run this script
if __name__ == "__main__":
    exit(main())

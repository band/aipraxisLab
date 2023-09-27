#! /usr/bin/env python
"""
initial code based on an example in this Medium post: <https://levelup.gitconnected.com/build-a-twitter-bot-for-arxiv-paper-summarization-by-openai-and-langchain-in-10-minutes-e57de6b32e03>
"""

# set up logging
import logging, sys
# logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate sentence topics from a text document.')
    parser.add_argument('--file', '-f', required=True, help='text file to be analyzed')
    parser.add_argument('--topics', '-t', required=True, help='topics to identify in document; one per line')
    return parser

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

import spacy
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.info(f"args: {args}")

    doc_file = str(args.file)
    document_text = read_file(doc_file)
    
    # Process the document with spaCy
    doc = nlp(document_text)

    # construct topic list from topic file
    with open(str(args.topics), "r") as file:
        topics = []
        for line in file:
            topics.append(f"{line.strip()}")

    logging.info(f"Topics: {topics}")

    # Function to identify sentences about specific topics
    def identify_sentences_about_topics(doc, topics):
        sentences_about_topics = {topic: [] for topic in topics}
    
        for sentence in doc.sents:
            for topic in topics:
                if topic.lower() in sentence.text.lower():
                    sentences_about_topics[topic].append(sentence.text)
    
        return sentences_about_topics

    # Identify sentences about the specified topics
    sentences_about_topics = identify_sentences_about_topics(doc, topics)

    # Print the sentences for each topic
    for topic, sentences in sentences_about_topics.items():
        print(f"Sentences about '{topic}':")
        for sentence in sentences:
            print(f"- {sentence}")
        print()

if __name__ == "__main__":
    exit(main())

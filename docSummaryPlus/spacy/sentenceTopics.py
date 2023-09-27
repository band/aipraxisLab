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
    return parser

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# TODO: read document text from text file

# Define the document text
"""
document_text =
In recent years, renewable energy sources such as solar and wind power have gained popularity as environmentally friendly alternatives to fossil fuels. Solar power is harnessed from the sun's energy, and it has become a cost-effective way to generate electricity. Wind power, on the other hand, relies on the kinetic energy of the wind to turn turbines and produce electricity. Fossil fuels, such as coal and oil, have been the dominant source of energy for decades, but they are known for their negative impact on the environment. Environmental sustainability is a growing concern, and the shift toward renewable energy sources is a step in the right direction.
"""
# build topics list
# TODO: read topic list from text file
# List of topics to identify in the document
# topics = ["Renewable Energy", "Solar Power", "Wind Power", "Fossil Fuels", "Environmental Sustainability"]


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

    # Open the file for reading
    with open("elements.txt", "r") as file:
        # Initialize an empty list to store the quoted elements
        topics = []
    # Loop through each line in the file
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

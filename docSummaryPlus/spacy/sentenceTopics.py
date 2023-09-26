import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# read document text file
# Define the document text
document_text = """
In recent years, renewable energy sources such as solar and wind power have gained popularity as environmentally friendly alternatives to fossil fuels. Solar power is harnessed from the sun's energy, and it has become a cost-effective way to generate electricity. Wind power, on the other hand, relies on the kinetic energy of the wind to turn turbines and produce electricity. Fossil fuels, such as coal and oil, have been the dominant source of energy for decades, but they are known for their negative impact on the environment. Environmental sustainability is a growing concern, and the shift toward renewable energy sources is a step in the right direction.
"""

# build topics list
# read topic list from text file
# List of topics to identify in the document
topics = ["Renewable Energy", "Solar Power", "Wind Power", "Fossil Fuels", "Environmental Sustainability"]

# Process the document with spaCy
doc = nlp(document_text)

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

#!/usr/bin/env/python

# set up logging
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# get env info
import os
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

import requests

def summarize_document(text):
    url = "https://api.cohere.ai/v1/summarize"
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "max_tokens": 255  # Adjust this value based on how long you want the summary to be
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["summary"]
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Replace with the text of your document
document_text = "Contrary to what we would like to believe, there is no such thing as a structureless group. Any group of people of whatever nature that comes together for any length of time for any purpose will inevitably structure itself in some fashion. The structure may be flexible; it may vary over time; it may evenly or unevenly distribute tasks, power and resources over the members of the group. But it will be formed regardless of the abilities, personalities, or intentions of the people involved. The very fact that we are individuals, with different talents, predispositions, and backgrounds makes this inevitable. Only if we refused to relate or interact on any basis whatsoever could we approximate structurelessness -- and that is not the nature of a human group. This means that to strive for a structureless group is as useful, and as deceptive, as to aim at an 'objective' news story, 'value-free' social science, or a 'free' economy. A 'laissez faire' group is about as realistic as a 'laissez faire' society; the idea becomes a smokescreen for the strong or the lucky to establish unquestioned hegemony over others. This hegemony can be so easily established because the idea of 'structurelessness' does not prevent the formation of informal structures, only formal ones. Similarly 'laissez faire' philosophy did not prevent the economically powerful from establishing control over wages, prices, and distribution of goods; it only prevented the government from doing so. Thus structurelessness becomes a way of masking power, and within the women\'s movement is usually most strongly advocated by those who are the most powerful whether they are conscious of their power or not). As long as the structure of the group is informal, the rules of how decisions are made are known only to a few and awareness of power is limited to those who know the rules. Those who do not know the rules and are not chosen for initiation must remain in confusion, or suffer from paranoid delusions that something is happening of which they are not quite aware."

def main():
    summary = summarize_document(document_text)
    print(summary)

if __name__ == "__main__":
    exit(main())

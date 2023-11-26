
# get env info
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
anthropic = Anthropic()

def show_completion(prompt):
    completion = anthropic.completions.create(model="claude-2",max_tokens_to_sample=1000,prompt=prompt)
    print(completion.completion)

text = 'During times of social migration, expecially if it is experienced as a migratory imperative, a occupation with identity develops. A general sense of mistrust and incohesion (Hopper, 1996) is experienced. Transformation is typified with a social feelings of being distanced, isolated and of spectatorship (as if the social is an object).  This brings to the fore a constellational dynamic during which members are becoming aware of their relatedness and affiliation within oragnizational and institutional structures. There is also an overbearing concern by management to control process and structure manifesting into strategy-as-dream. It is proposed that the constellational dynamic has a discernible manifestation in both the organization and institution and that is helpful to differentiate the two.'

prompt = f"{HUMAN_PROMPT} list key themes in this text: {text}{AI_PROMPT}"

show_completion(prompt)



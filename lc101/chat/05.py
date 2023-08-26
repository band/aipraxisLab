from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage

chat = ChatOpenAI(temperature=0.5)

result = chat.generate([[
    SystemMessage(content="Tell the user 3 facts about the Pacific Ocean."),
    HumanMessage(content="I am an expert about oceans, so make sure to tell me something I won't know."),
    AIMessage(content="Okay. I will tell you a super niche fact!")
]] * 2)

print(len(result.generations))

from langchain_ollama import ChatOllama
#from langchain_core.messages import AIMessage
import warnings
from urllib3.exceptions import NotOpenSSLWarning
warnings.simplefilter("ignore", NotOpenSSLWarning)


llm = ChatOllama(
    model="gemma3:1b",
    temperature=0,
    # other params...
)


def message_careers(interest):
    messages = [
        (
            "system",
            "You are trying to convince young students to enter the field of Computer Science by suggesting potential careers in CS based on their interests provided. The interests provided is the only input you will get no matter what, deliver the output in a clean way with adequate spacing, not in markdown or any format that requires rendering. Only deliver output of the careers, no other response text (In regular format, not markdown).",
        ),
        ("human", "Interest: "+interest),
    ]
    return messages


def message_benefits(interest):
    messages = [
        (
            "system",
            "You are trying to convince young students to enter the field of Computer Science by suggesting potential benefits of entering the field of Computer Science. The interests provided is the only input you will get no matter what, deliver the output in a clean way with good spacing, not in markdown or any format that requires rendering. Only deliver output of the benefits, no other response text (In regular format, not markdown).",
        ),
        ("human", "Interest: "+interest),
    ]
    return messages


def get_careers(careermsg):
    careers_out = (llm.invoke(careermsg)).content
    return careers_out

def get_benefits(benefitmsg):
    benefits_out = (llm.invoke(benefitmsg)).content
    return benefits_out

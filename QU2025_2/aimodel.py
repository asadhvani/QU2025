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
            "Provide a 100 word summary of computer science careers for kids’. Provide in div tags format. Don’t provide Explanation of the div tags structure. Provide answer based on interests provided.",
        ),
        ("human", "Interests (For Career Rankings): "+interest),
    ]
    return messages


def message_benefits(interest):
    messages = [
        (
            "system",
            "Provide a convincing 100 word summary for kids to consider computer science.  Provide in div tags format. Provide a output based on interests provided. Don’t provide Explanation of the div tags structure.",
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




#Template From Docs
#if not os.environ.get("OPENAI_API_KEY"):
    #os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
def run_llm(inpt):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
        # base_url="...",
        # organization="...",
        # other params...
    )

    messages = [
        (
            "system",
            "You are a person trying to encourage an aspiring student to enter the field of CS. Respond to the prompts in markdown.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    msg_content=str(ai_msg.content)
    return msg_content
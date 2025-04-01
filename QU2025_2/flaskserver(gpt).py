import langchain as lc
import numpy as np
import pandas as pd
import torch
import os
import getpass
from langchain_openai import ChatOpenAI
from flask import Flask, request, send_file, redirect
import markdown

app = Flask(__name__)

# Your function: Processes input before generating Markdown
def process_and_generate_md(user_input):
    """ Custom processing before Markdown conversion. """
    processed_text = user_input[::-1]  # Example: Reverse input (replace with your logic)
    
    md_content = f""" # Processed Markdown Output  
    
**Processed Input:** {processed_text}  

## Example Generated Content  
- Processed: {processed_text[:5]}...  
- Length: {len(user_input)} characters  
"""
    return md_content

def run_llm(inpt):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key="",  # if you prefer to pass api key in directly instaed of using env vars
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
    
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["input_text"]

        # Step 1: Process input and generate Markdown
        md_content = run_llm(user_input)

        # Step 2: Convert Markdown to HTML
        html_content = markdown.markdown(md_content)

        # Step 3: Save as 'output.html'
        with open("output.html", "w") as f:
            f.write(html_content)

        return redirect("/")  # Reload the page to update iframe

    return """
    <form method="post">
        <input type="text" name="input_text" placeholder="Enter text">
        <button type="submit">Submit</button>
    </form>
    <iframe src="/output" id="outputFrame"></iframe>
    """

@app.route("output.html")
def serve_output():
    return send_file("output.html")

if __name__ == "__main__":
    app.run(debug=True)
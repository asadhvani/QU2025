
"""
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Set up templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "output": None})

@app.post("/process/", response_class=HTMLResponse)
def process(request: Request, text: str = Form(...)):
    processed_text = text.upper()  # Example: Convert text to uppercase
    return templates.TemplateResponse("index.html", {"request": request, "output": processed_text})
"""
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import aimodel as ai

stored_text="No input provided"
app = FastAPI()

# Mount the static directory to serve pre-existing HTML files
#app.mount("/static", StaticFiles(directory="templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
#app.mount("/Media", StaticFiles(directory="Media"), name="Media")
# Initialize Jinja2Templates to render HTML templates
templates = Jinja2Templates(directory="templates")


# Serve the main input page
@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Handle form submission and show first output
"""
@app.post("/process/")
def process_data(request: Request, text: str = Form(...)):
    print(text)
    processed_text1 = text.upper()  # Convert text to uppercase
    return templates.TemplateResponse("submitted.html", {"request": request, "output": processed_text1})#Set to go to a your response has been submitted page
"""

@app.post("/process/")
def process_data(request: Request, text: str = Form(...)):
    global careers_text
    global benefits_text
    print(text)
    global stored_text
    stored_text = text# Store the text for later use
    if text=="No input provided":
        benefits_text="No input provided"
        careers_text="No input provided"
    else:
        benefits_text=ai.get_benefits(ai.message_benefits(text))
        careers_text=ai.get_careers(ai.message_careers(text))
        print("Benefts: "+benefits_text)
        print("Careers: "+careers_text)
    return templates.TemplateResponse("submitted.html", {"request": request, "output": text})  # Set to go to a your response has been submitted page
@app.get("/output1", response_class=HTMLResponse)
def show_output1(request: Request):
    global careers_text
    #processed_text2 = stored_text.upper() if stored_text else "No input provided"
    #if stored_text == "No input provided":
        #processed_text2 = "No input provided"
    #else:
        #processed_text2 = ai.get_benefits(ai.message_benefits(stored_text))
        #print("Benefts: "+processed_text2)
    return templates.TemplateResponse("output1.html", {"request": request, "output": careers_text})

"""
# Serve second output page
@app.get("/output2", response_class=HTMLResponse)
def show_output2(request: Request, text: str):
    processed_text2 = text[::-1]  # Reverse text
    return templates.TemplateResponse("output2.html", {"request": request, "output": processed_text2})

"""

@app.get("/output2", response_class=HTMLResponse)
def show_output2(request: Request):
    global benefits_text
    #processed_text2 = stored_text[::-1] if stored_text else "No input provided"
    """
    if stored_text == "No input provided":
        processed_text2 = "No input provided"
    else:
        processed_text2 = ai.get_careers(ai.message_careers(stored_text))
        print("Careers: "+processed_text2)
    """
    return templates.TemplateResponse("output2.html", {"request": request, "output": benefits_text})

# Serve the three additional pages
@app.get("/page1", response_class=HTMLResponse)
def serve_page1(request: Request):
    return templates.TemplateResponse("benefits.html", {"request": request})


@app.get("/page2", response_class=HTMLResponse)
def serve_page2(request: Request):
    return templates.TemplateResponse("career.html", {"request": request})



@app.get("/page3", response_class=HTMLResponse)
def serve_page3(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

"""
@app.get("/index-css", response_class=HTMLResponse)
def serve_page3(request: Request):
    return templates.TemplateResponse("/static/index_style.css", {"request": request})
"""
print("Running")


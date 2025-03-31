
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

app = FastAPI()

# Mount the static directory to serve pre-existing HTML files
app.mount("/static", StaticFiles(directory="templates"), name="templates")

# Initialize Jinja2Templates to render HTML templates
templates = Jinja2Templates(directory="templates")


# Serve the main input page
@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Handle form submission and show first output
@app.post("/process/")
def process_data(request: Request, text: str = Form(...)):
    print(text)
    processed_text1 = text.upper()  # Convert text to uppercase
    return templates.TemplateResponse("submitted.html", {"request": request, "output": processed_text1})#Set to go to a your response has been sumitted page

@app.post("/output1/")
def process_data(request: Request, text: str = Form(...)):
    processed_text1 = text.upper()  # Convert text to uppercase
    return templates.TemplateResponse("output1.html", {"request": request, "output": processed_text1})


# Serve second output page
@app.get("/output2/", response_class=HTMLResponse)
def show_output2(request: Request, text: str):
    processed_text2 = text[::-1]  # Reverse text
    return templates.TemplateResponse("output2.html", {"request": request, "output": processed_text2})


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

print("Running")


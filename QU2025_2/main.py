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

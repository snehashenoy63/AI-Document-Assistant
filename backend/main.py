from fastapi import FastAPI, UploadFile, File
from pdf_processor import extract_text
from chatbot import ask_gemini

app = FastAPI()

document_text = ""

@app.get("/")
def home():
    return {"message": "AI Document Assistant Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global document_text

    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)

    document_text = extract_text(filepath)

    return {
        "filename": file.filename,
        "characters": len(document_text),
        "stored": len(document_text)
    }

@app.get("/ask")
def ask(question: str):

    global document_text

    answer = ask_gemini(question, document_text)

    return {
        "question": question,
        "answer": answer
    }
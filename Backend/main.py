from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import uuid
from ocr import extract_easyocr, extract_pytesseract
from utils import fuse_ocr
from llm import explain_text


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    file_id = f"/tmp/{uuid.uuid4()}_{file.filename}"
    with open(file_id, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    easy_text = extract_easyocr(file_id)
    tess_text = extract_pytesseract(file_id)

    fused_text = fuse_ocr(easy_text, tess_text)
    explanation = explain_text(fused_text)

    return {
        "extracted_text": fused_text,
        "explanation": explanation
    }
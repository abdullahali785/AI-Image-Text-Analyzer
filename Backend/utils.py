import re


def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def fuse_ocr(easyocr_text: list[str], tesseract_text: str) -> str:
    easyocr_joined = " ".join(easyocr_text)
    combined = f"{easyocr_joined} {tesseract_text}"
    return clean_text(combined)

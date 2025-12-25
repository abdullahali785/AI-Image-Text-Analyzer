from ocr import extract_easyocr, extract_pytesseract
from utils import fuse_ocr
from llm import explain_text


def image_to_explanation(image_path: str) -> str:
    easy = extract_easyocr(image_path)
    tess = extract_pytesseract(image_path)
    fused_text = fuse_ocr(easy, tess)
    return explain_text(fused_text)

if __name__ == "__main__":
    print(image_to_explanation("Images/short-inspirational-quotes-7.jpg"))

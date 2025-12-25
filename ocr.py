from PIL import Image
import pytesseract
import easyocr


def extract_pytesseract(image_path: str) -> str:
    image = Image.open(image_path)
    return pytesseract.image_to_string(image).strip()


def extract_easyocr(image_path: str) -> list[str]:
    reader = easyocr.Reader(['en'], gpu=False)
    return reader.readtext(image_path, detail=0)

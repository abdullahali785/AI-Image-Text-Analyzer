from openai import OpenAI
import pytesseract, easyocr
from PIL import Image

client = OpenAI(api_key=open("api_key.csv").read().strip())
image_path = "Images/short-inspirational-quotes-7.jpg"


def text_pytesseract(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def text_easyocr(image_path):
    reader = easyocr.Reader(['en'])
    return reader.readtext(image_path, detail=0)


def pytesseract_tool(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    
    import openai

    openai.api_key = open('api_key.csv','r').read()
    user_input = f"Hi, I found an image that says '{extracted_text}'. Can you please explain the image in words."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return(response.choices[0].message["content"])

def easyocr_tool(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)

    import openai

    openai.api_key = open('api_key.csv','r').read()
    user_input = f"Hi, I found an image that says '{result}'. Can you please explain the image in words."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return(response.choices[0].message["content"])


def AI(text_easyocr, text_pytesseract):
    user_input = (
        f"I found an image.\n\n"
        f"EasyOCR detected: {text_easyocr}\n"
        f"Pytesseract detected: {text_pytesseract}\n\n"
        f"Explain the text and what the image likely represents."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


def image_to_text(image_path):
    easyocr = text_easyocr(image_path)
    pytesseract = text_pytesseract(image_path)

    return AI(easyocr, pytesseract)

print(image_to_text("Images/short-inspirational-quotes-7.jpg"))
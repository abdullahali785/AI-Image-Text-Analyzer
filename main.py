def AI(text_EasyOCR, text_pytesseract):
    import openai

    openai.api_key = open('api_key.csv','r').read()
    user_input = f"I found an image that says '{text_EasyOCR}' using 'EasyOCR' and '{text_pytesseract}' using 'pytesseract'. Explain the content of the image, including the text it says."
    # user_input = input('Prompt: ')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
            ]
        )
    return(response.choices[0].message["content"])

#print(AI())

image_path = '/Users/abdullahali/Downloads/sqz78.jpg'

def image_to_text_pytesseract(image_path):
    from PIL import Image
    import pytesseract

    # Load image
    image = Image.open(image_path)
    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

#print(image_to_text_pytesseract())

def image_to_text_easyocr(image_path):
    import easyocr
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)
    return result 

#print(image_to_text_easyocr())

def pytesseract_tool(image_path):
    from PIL import Image
    import pytesseract

    # Load image
    image = Image.open(image_path)
    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    
    import openai

    openai.api_key = open('api_key.csv','r').read()
    user_input = f"Hi, I found an image that says '{extracted_text}'. Can you please explain the image in words."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
            ]
        )
    return(response.choices[0].message["content"])
    #return user_input

#print(pytesseract_tool('/Users/abdullahali/Downloads/bold-d-thursday-text-against-clean-white-background-bold-d-thursday-text-against-clean-white-background-331064540.jpg.webp'))

def easyocr_tool(image_path):
    import easyocr
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)

    import openai

    openai.api_key = open('api_key.csv','r').read()
    user_input = f"Hi, I found an image that says '{result}'. Can you please explain the image in words."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
            ]
        )
    return(response.choices[0].message["content"])

#print(easyocr_tool('/Users/abdullahali/Downloads/bold-d-thursday-text-against-clean-white-background-bold-d-thursday-text-against-clean-white-background-331064540.jpg.webp'))

def image_to_text(image_path):
    result = image_to_text_easyocr(image_path)

    extracted_text = image_to_text_pytesseract(image_path)

    return(AI(result, extracted_text))

print(image_to_text('/Users/abdullahali/Downloads/sqz78.jpg'))
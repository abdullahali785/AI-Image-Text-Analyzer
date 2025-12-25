from openai import OpenAI

client = OpenAI(api_key=open("api_key.csv").read().strip())

def explain_text(text: str) -> str:
    prompt = (
        "The following text was extracted from an image.\n\n"
        f"Text:\n{text}\n\n"
        "Explain what the image is conveying in clear, natural language."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content
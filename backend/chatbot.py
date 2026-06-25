import google.generativeai as genai

genai.configure(api_key="YOUR_ACTUAL_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(question, context):

    prompt = f"""
    Answer the question using only the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


def make_good(text):
    try:
        api_key = ""
        text = f"Summarize the reviews\n{text}"
        genai.configure(api_key=api_key)
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        }

        model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings)
        response = model.generate_content(text)

        return response.text
    except ValueError:
        print("please try again after sometime.")

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


def make_good(text):
    try:
        # api 1: AIzaSyBNbNNUCp_sEBz2luE9m-8-UXLgZ9R7Vlo
        # api 2: AIzaSyDcEQhNMWZLiAfISxumMJaUTGf5YhK8XAI
        # api 3: AIzaSyAs83PgRKmJyLFBbenPFJSoWk6n_ktkbUc

        text = f"Summarize the reviews\n{text}"
        genai.configure(api_key="AIzaSyBNbNNUCp_sEBz2luE9m-8-UXLgZ9R7Vlo")
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        }

        model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings)
        response = model.generate_content(text)

        return response.text
    except ValueError:
        print("wait some time.")

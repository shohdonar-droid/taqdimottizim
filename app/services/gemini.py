import os
from google import genai
from app.config.config import GEMINI_API_KEY

class GeminiService:
    def __init__(self):
        if GEMINI_API_KEY:
            self.client = genai.Client(api_key=GEMINI_API_KEY)
        else:
            self.client = None

    def generate_response(self, text: str, context: str = "Sen o'zbek tilidagi yordamchisan.") -> str:
        if not self.client:
            return "Kechirasiz, Gemini API xizmati sozlanmagan."
        try:
            prompt = f"{context}\n\nFoydalanuvchi so'rovi: {text}"
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            return f"Kechirasiz, AI xizmatida xatolik yuz berdi: {e}"

gemini_service = GeminiService()

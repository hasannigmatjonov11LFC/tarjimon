from googletrans import Translator
from googletrans.client import LANGUAGES

async def tarjimon(user_text, user_lang):
    translator = Translator()
    natija = await translator.translate(text=user_text, dest=user_lang)
    return natija.text

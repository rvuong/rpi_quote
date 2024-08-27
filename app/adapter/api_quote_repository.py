import requests
import os
from app.domain.quote_repository import QuoteRepository
from app.domain.quote import Quote
from dotenv import load_dotenv
from translate import Translator

class ApiQuoteRepository(QuoteRepository):
    def __init__(self):
        load_dotenv()
        self.APP_ENV = os.getenv('APP_ENV')
        self.APP_LANG = os.getenv('APP_LANG')
        self.API_URL = os.getenv('QUOTE_API_URL')

    def get(self) -> Quote:
        # Get Quote
        if self.APP_ENV == 'dev':
            self.quote = Quote(text='Everyone you admire was once a beginner.', author='Jack Butcher')
        else:
            response = requests.get(self.API_URL)

            if response.status_code == 200:
                data = response.json()[0]
                self.quote = Quote(text=data['q'], author=data['a'])
            else:
                raise Exception("Could not fetch a quote from the API.")

        # Translate Quote
        if self.APP_LANG != 'en':
            translator = Translator(to_lang=self.APP_LANG)
            self.quote = Quote(text=translator.translate(self.quote.get_text()), author=translator.translate(self.quote.get_author()))

        return self.quote

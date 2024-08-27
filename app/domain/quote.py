class Quote:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author

    def __str__(self):
        return f'"{self.text}"\n - {self.author}'

    def get_text(self):
        return self.text

    def get_author(self):
        return self.author

from app.domain.display import Display
from app.domain.quote import Quote

class ConsoleDisplay(Display):
    def show(self, quote: Quote):
        print(f'{quote}')

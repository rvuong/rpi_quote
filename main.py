from app.adapter.api_quote_repository import ApiQuoteRepository
from app.adapter.console_display import ConsoleDisplay

def main():
    display = ConsoleDisplay()

    # Get Quote
    quote_repository = ApiQuoteRepository()
    quote = quote_repository.get()

    # Send to stdout/terminal
    display.show(quote)

if __name__ == '__main__':
    main()

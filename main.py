import sys
from app.adapter.api_quote_repository import ApiQuoteRepository
from app.adapter.epaper_display import EpaperDisplay

def main(action: str):
    display = EpaperDisplay()

    match action:
        case "clear":
            display.clear()
        case _:
            # Get Quote
            quote_repository = ApiQuoteRepository()
            quote = quote_repository.get()

            # Send to stdout/terminal
            display.show(quote)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "clear":
        main("clear")
    else:
        main("show")

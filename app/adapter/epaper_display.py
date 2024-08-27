import logging
import os
import sys
import textwrap
import time
from app.domain.display import Display
from app.domain.quote import Quote
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd7in5_V2

assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '../assets')

class EpaperDisplay(Display):
    MAX_LINE_LENGTH = 26
    FONT_HEIGHT_QUOTE = 54
    FONT_SPACE_QUOTE = 12
    FONT_HEIGHT_AUTHOR = 36
    FONT_SPACE_AUTHOR = 8
    QUOTE_X = 50

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Init e-Paper display...")

        self.epd = epd7in5_V2.EPD()
        self.epd.init()
        logging.info(f'EPD width: {self.epd.width}')
        logging.info(f'EPD height: {self.epd.height}')

    def show(self, quote: Quote):
        max_line_length = self.MAX_LINE_LENGTH
        font_height_quote = self.FONT_HEIGHT_QUOTE
        font_space_quote = self.FONT_SPACE_QUOTE
        font_height_author = self.FONT_HEIGHT_AUTHOR
        font_space_author = self.FONT_SPACE_AUTHOR

        font_quote = ImageFont.truetype(os.path.join(assets_dir, 'Font.ttc'), font_height_quote)
        font_author = ImageFont.truetype(os.path.join(assets_dir, 'Font.ttc'), font_height_author)

        Himage = Image.new('1', (self.epd.width, self.epd.height), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)

        # Split the quote into chunks of a maximal length
        lines = textwrap.wrap(quote.get_text(), width=max_line_length)

        # Get quote coordinates
        quote_height = len(lines) * (font_height_quote + font_space_quote)

        while quote_height >= self.epd.height:
            max_line_length = max_line_length * 2
            font_height_quote = int(font_height_quote / 2)
            font_space_quote = int(font_space_quote / 2)
            font_height_author = int(font_height_author / 2)
            font_space_author = int(font_space_author / 2)
            font_quote = ImageFont.truetype(os.path.join(assets_dir, 'Font.ttc'), font_height_quote)
            font_author = ImageFont.truetype(os.path.join(assets_dir, 'Font.ttc'), font_height_author)

            # Split the quote into chunks of a maximal length
            lines = textwrap.wrap(quote.get_text(), width=max_line_length)
            # Get quote coordinates
            quote_height = len(lines) * (font_height_quote + font_space_quote)

        quote_y = (self.epd.height - quote_height) / 2

        for line in lines:
            draw.text((self.QUOTE_X, quote_y), line, font = font_quote, fill = 0)
            quote_y += (font_height_quote + font_space_quote)

        # Display author
        author_y = quote_y
        draw.text((self.QUOTE_X, author_y + font_space_author), quote.get_author(), font = font_author, fill = 0)

        # Final drawing
        self.epd.display(self.epd.getbuffer(Himage))
        self.epd.sleep()

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 128x32 display with hardware I2C
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
disp.begin()

# Clear the display
disp.clear()
disp.display()

display_width = disp.width
display_height = disp.height

# Create a blank image which fills the screen as a drawing surface 
# Mode '1' represents 1-bit color
image = Image.new('1', (display_width, display_height))

# Get drawing object
draw = ImageDraw.Draw(image)

# Load font
# font = ImageFont.truetype('fonts/VCR_OSD_MONO_1.001.ttf', 21)
font = ImageFont.truetype('fonts/Perfect DOS VGA 437.ttf', 16)

# Calculate co-ordinates to draw text in the centre of the display
def get_text_coordinates(text):
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (display_width / 2) - (text_width / 2)
    text_y = (display_height / 2) - (text_height / 2)
    return (text_x, text_y)

def display_text(text):
    clear_display()
    coords = get_text_coordinates(text)
    draw.text(coords, text, font=font, fill=255)
    disp.image(image)
    disp.display()

def clear_display():
    draw.rectangle((0, 0, display_width, display_height), outline=0, fill=0)
    disp.image(image)
    disp.display()

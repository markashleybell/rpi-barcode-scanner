
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

width = disp.width
height = disp.height

# Create blank image for drawing (mode '1' represents 1-bit color)
image = Image.new('1', (width, height))

# Get drawing object
draw = ImageDraw.Draw(image)

# Clear the image
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Load font
font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf', 21)

draw.text((14, 8), "12345678", font=font, fill=255)

disp.image(image)
disp.display()

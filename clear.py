
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


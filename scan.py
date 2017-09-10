import string
import constants

from evdev import InputDevice, ecodes
from evdev.util import categorize
from oleddisplay import display_text, clear_display

display_text("Ready")

values = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

device = InputDevice('/dev/input/by-id/usb-USB_Adapter_USB_Device-event-kbd')

output = []

try:
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY and event.value == constants.UP:
            if event.code == ecodes.KEY_ENTER:
                display_text(''.join(output))
                output = []
            else:
                output.append(values[event.code])
except:   
    clear_display() 
    print("EXIT")

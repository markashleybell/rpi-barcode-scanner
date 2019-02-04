import string
import constants
import requests

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
                code = ''.join(output)
                display_text(code)
                requests.post('http://192.168.78.12:8080/registercode', data = {'code': code})
                output = []
            else:
                output.append(values[event.code])
except:   
    clear_display() 
    print("EXIT")

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from luma.core.virtual import viewport
import time

serial = spi(port=0, device=0)
device = ssd1309(serial)


virtual = viewport(device, width=device.width, height=768)
x = 1000
while (True):
    with canvas(virtual) as draw:
        draw.text((0, 25), "say hello to my little friend", fill="white")
    x = x - 1
    time.sleep(0.1)

import Maker_Pi as makerpi  # Set up BEAPER Pico I/O
from time import sleep_ms
from math import sin, radians, pi

# while True:
#     for i in range(360):
#         rad = radians(i)
#         r = int((sin(rad) + 1) / 2 * 0xFF)
#         g = int((sin(rad + 2 * pi / 3) + 1) / 2 * 0xFF)
#         b = int((sin(rad + 4 * pi / 3) + 1) / 2 * 0xFF)
#         makerpi.NEOPIXELS.fill((r, g, b))
#         makerpi.NEOPIXELS.write()
#         sleep_ms(10)

# while True:
#     for i in range(360):
#         rad = radians(i)
#         makerpi.NEOPIXELS.fill((int(sin(rad) * 0xFF), int(sin(rad + 2 * pi / 3) * 0xFF), int(sin(rad + 4 * pi / 3) * 0xFF)))
#         makerpi.NEOPIXELS.write()
#         sleep_ms(10)

# makerpi.neopixel_set_color(makerpi.GREEN, 1)
# makerpi.neopixel_set_color(makerpi.BLUE, 0)
makerpi.NEOPIXEL.write()





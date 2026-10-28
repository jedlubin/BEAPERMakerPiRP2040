import Maker_Pi as makerpi  # Set up BEAPER Pico I/O
from time import sleep

makerpi.beep(1300)

while True:
    print(f'SW1: {makerpi.SWITCH1.value()}\nSW2: {makerpi.SWITCH2.value()}')
    sleep(0.3)
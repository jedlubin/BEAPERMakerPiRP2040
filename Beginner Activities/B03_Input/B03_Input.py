# ================================================================================
# Beginner Activity 3: Digital Input [Activity_B03_Input.py]
# Version: 0.1
# Updated: October 28, 2026
#
# Platform: Cytron Maker Pi RP2040
# Requires: Maker_Pi.py board module file
# ================================================================================

# IMPORTANT: Copy Maker_Pi.py into your Maker Pi board.
import Maker_Pi as makerpi  # Set up BEAPER Pico I/O

import time

while True:
    # Momentary button SWITCH1 (labeled GP20)
    if makerpi.SWITCH_GP20.value() == 0:
        makerpi.LED_GP2.value(1)
    else:
        makerpi.LED_GP2.value(0)

    # Start a pattern
    if makerpi.SWITCH_GP21.value() == 0:
        makerpi.LED_GP2.value(1)
        time.sleep(0.2)
        makerpi.LED_GP3.value(1)
        time.sleep(0.2)
        makerpi.LED_GP4.value(1)
        time.sleep(0.2)
        makerpi.LED_GP5.value(1)
        time.sleep(0.2)
        makerpi.LED_GP2.value(0)
        time.sleep(0.2)
        makerpi.LED_GP3.value(0)
        time.sleep(0.2)
        makerpi.LED_GP4.value(0)
        time.sleep(0.2)
        makerpi.LED_GP5.value(0)
        time.sleep(0.2)

    time.sleep_ms(20)  # Short delay for button debouncing

# ================================================================================
# Beginner Activity 2: Timing (Blocking) [Activity_B02_Timing.py]
# Version: 0.1
# Updated: October 28, 2026
# 
# Platform: Cytron Maker Pi RP2040
# Requires: Maker_Pi.py board module file
# ================================================================================

# IMPORTANT: Copy Maker_Pi.py into your Maker Pi board.
import Maker_Pi as makerpi  # Set up Maker Pi

import time  # Import time functions

# Main loop - code indented below while True: repeats forever
while True:
    makerpi.LED2.value(1)
    makerpi.LED5.value(0)
    time.sleep(0.5)        # wait 0.5 seconds

    makerpi.LED2.value(0)
    makerpi.LED5.value(1)
    time.sleep(0.5)        # wait 0.5 seconds


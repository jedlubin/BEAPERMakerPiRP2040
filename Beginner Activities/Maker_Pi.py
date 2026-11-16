# ==============================================================================
# Maker Pi RP2040 Board Module [Maker_Pi.py]
# Version: 0.1
# Updated: November 16, 2026
# 
# Board support module for using the Cytron Maker Pi RP 2040. Based on the  
# mirobo.tech BEAPER Pico module and beginner microcontroller curriculum. 
# 
# This module aims to configures Maker Pi's on-board circuits with
# simple, intuitive names, and provides simple helper functions to enable
# beginners to focus on learning programming concepts quickly.
# 
# Before getting started with it you should know:
# - nothing here is hidden, or **magic**, or requires special libraries
# - the functions are just normal Python code to help you start learning
# - you're encouraged to modify the code to make it work better for you!
# 
# Hardware notes:
# - Buttons use internal pull-up resistors (pressed == 0)
# - LEDs, GPIO, and motor driver share I/O pins (so much I/O, so few I/O pins!)
# ==============================================================================

from machine import Pin, ADC, PWM
import neopixel
import time

# ------------------------------------------------------------------------------
# NeoPixel RGB LEDs
# ------------------------------------------------------------------------------

NEOPIXEL_PIN = const(18)
# Note: const() stores fixed values in ROM to save RAM

NEOPIXEL = neopixel.NeoPixel(Pin(NEOPIXEL_PIN, Pin.OUT), 2)

WHITE = (255, 255, 255)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =  (0, 0, 255)
OFF =   (0, 0, 0)

def neopixel_set_color(rgb, i=None):
    if i == None:
        NEOPIXEL.fill(rgb)
    else:
        NEOPIXEL[i] = rgb
    NEOPIXEL.write()

def neopixel_off():
    neopixel_set_color(OFF)

# ------------------------------------------------------------------------------
# LEDs (Digital IO Status)
# ------------------------------------------------------------------------------

# IMPORTANT: LED pins are shared with GPIO pins. Using the
# LEDs will affect other components' behavior!

LED_GP0_PIN = const(0)  # LED on GPIO 0
LED_GP1_PIN = const(1)  # LED on GPIO 1
LED_GP2_PIN = const(2)  # LED on GPIO 2
LED_GP3_PIN = const(3)  # LED on GPIO 3
LED_GP4_PIN = const(4)  # LED on GPIO 4
LED_GP5_PIN = const(5)  # LED on GPIO 5
LED_GP6_PIN = const(6)  # LED on GPIO 6
LED_GP7_PIN = const(7)  # LED on GPIO 7
LED_GP16_PIN = const(16)  # LED on GPIO 16
LED_GP17_PIN = const(17)  # LED on GPIO 17
LED_GP26_PIN = const(26)  # LED on GPIO 26
LED_GP27_PIN = const(27)  # LED on GPIO 27
LED_GP28_PIN = const(28)  # LED on GPIO 28

LED_GP0 = Pin(LED_GP0_PIN, Pin.OUT)
LED_GP1 = Pin(LED_GP1_PIN, Pin.OUT)
LED_GP2 = Pin(LED_GP2_PIN, Pin.OUT)
LED_GP3 = Pin(LED_GP3_PIN, Pin.OUT)
LED_GP4 = Pin(LED_GP4_PIN, Pin.OUT)
LED_GP5 = Pin(LED_GP5_PIN, Pin.OUT)
LED_GP6 = Pin(LED_GP6_PIN, Pin.OUT)
LED_GP7 = Pin(LED_GP7_PIN, Pin.OUT)
LED_GP16 = Pin(LED_GP16_PIN, Pin.OUT)
LED_GP17 = Pin(LED_GP17_PIN, Pin.OUT)
LED_GP26 = Pin(LED_GP26_PIN, Pin.OUT)
LED_GP27 = Pin(LED_GP27_PIN, Pin.OUT)
LED_GP28 = Pin(LED_GP28_PIN, Pin.OUT)

LEDS = (LED_GP0, LED_GP1, LED_GP2, LED_GP3, LED_GP4, LED_GP5, LED_GP6, LED_GP7,
        LED_GP16, LED_GP17, LED_GP26, LED_GP27, LED_GP28)  # Tuple of all LED pins.
# Useful for iterating through all LEDS - see below:

def leds_on():
    # Turn all four LEDs on
    for led in LEDS:
        led.on()
        
def leds_off():
    # Turn all four LEDs off
    for led in LEDS:
        led.off()

# ------------------------------------------------------------------------------
# Pushbutton Switches
# ------------------------------------------------------------------------------

# All pushbutton switches use internal pull-up resistors (active-LOW)

SW_GP20_PIN = const(20)
SW_GP21_PIN = const(21)

SWITCH_GP20 = Pin(SW_GP20_PIN, Pin.IN, Pin.PULL_UP)
SWITCH_GP21 = Pin(SW_GP21_PIN, Pin.IN, Pin.PULL_UP)

SWITCHES = (SWITCH_GP20, SWITCH_GP21)  # Tuple of all pushbutton switch pins.
# Useful for iterating through all SWITCHES - see LEDS examples, above.


# ------------------------------------------------------------------------------
# Motor Controller
# ------------------------------------------------------------------------------

# NOTE: The forward and reverse directions of each motor are dependent
# on both program code and physical motor wiring connections on CON1.

M1A_PIN = const(8)
M1B_PIN = const(9)
M2A_PIN = const(10)
M2B_PIN = const(11)

M1A = Pin(M1A_PIN, Pin.OUT)  # Left motor terminal A
M1B = Pin(M1B_PIN, Pin.OUT)  # Left motor terminal B
M2A = Pin(M2A_PIN, Pin.OUT)  # Right motor terminal A
M2B = Pin(M2B_PIN, Pin.OUT)  # Right motor terminal B

# Motor helper functions

def motors_stop():
    M1A.value(0)
    M1B.value(0)
    M2A.value(0)
    M2B.value(0)

def left_motor_forward():
    M1A.value(1)
    M1B.value(0)

def left_motor_reverse():
    M1A.value(0)
    M1B.value(1)
    
def left_motor_stop():
    M1A.value(0)
    M1B.value(0)

def right_motor_forward():
    M2A.value(0)
    M2B.value(1)  # Opposite of left_motor_forward()

def right_motor_reverse():
    M2A.value(1)  # Opposite of left_motor_reverse()
    M2B.value(0)

def right_motor_stop():
    M2A.value(0)
    M2B.value(0)
    

# ------------------------------------------------------------------------------
# Piezo Speaker
# ------------------------------------------------------------------------------

# Generate tones using PWM (similar to Arduino tone() functions)

SPEAKER_PIN = const(22)

SPEAKER = PWM(Pin(SPEAKER_PIN), duty_u16=0)

def tone(frequency, duration=None):
    # Start a tone at specified frequency (Hz), and stop the tone after
    # an optional duration (ms). Adding duration causes a blocking delay.
    SPEAKER.freq(frequency)
    SPEAKER.duty_u16(32768)
    if duration is not None:
        time.sleep_ms(duration)
        noTone()

def noTone(duration=None):
    # Stop the tone. Optionally pause (blocking) for the duration (ms). 
    SPEAKER.duty_u16(0)
    if duration is not None:
        time.sleep_ms(duration)

def beep(duration=100):
    # Play a short beep (100ms by default)
    tone(1000, duration)

# ------------------------------------------------------------------------------
# Analog Inputs
# ------------------------------------------------------------------------------

ADC0_PIN = const(26)
ADC1_PIN = const(27)
ADC2_PIN = const(28)

# Raspberry Pi Pico analog inputs
ADC0 = ADC(Pin(ADC0_PIN))
ADC1 = ADC(Pin(ADC1_PIN))
ADC2 = ADC(Pin(ADC2_PIN))
VSYS = ADC(Pin(29))   # Pico voltage regulator input (VSYS / 3)
MCU_TEMP = ADC(ADC.CORE_TEMP)  # RP2xxxx die temperator sensor

# Analog helper functions

def VSYS_volts():
    # Read converted system voltage in volts.
    return VSYS.read_u16() * 9.9 / 65535

def mcu_temperature():
    # Read MCU die temp in degrees C. From the Raspberry Pi Pico datasheet:
    # "The temperature sensor measures the Vbe voltage of a biased bipolar
    # diode, connected to the fifth ADC channel. Typically, Vbe = 0.706V
    # at 27 degrees C, with a slope of -1.721mV (0.001721) per degree."
    mcu_temp_volts = MCU_TEMP.read_u16() * 3.3 / 65535
    return 27 - (mcu_temp_volts - 0.706) / 0.001721

# ------------------------------------------------------------------------------
# 5V Digital Output Headers (supports up to 4 servos)
# ------------------------------------------------------------------------------

# 5V Digital output headers (output only)
SERVO_GP12_PIN = const(12)  # Servo 1
SERVO_GP13_PIN = const(13)  # Servo 2
SERVO_GP14_PIN = const(14)  # Servo 3
SERVO_GP15_PIN = const(15)  # Servo 4

# Servo pulse width constants (microseconds). Adjust for your servo.
# Standard 90-degree servo: 1000us to 2000us
SERVO_MIN_US = const(1000)   # Pulse width at 0 degrees
SERVO_MAX_US = const(2000)   # Pulse width at maximum angle
SERVO_RANGE  = const(90)     # Maximum servo angle (degrees)

# Servos are initialized to centre position (duty_u16=4915 ≈ 1.5ms).
# This value is calculated from: 
#   - pulse period: 1 / 50Hz pulse frequency = 20ms period
#   - 1.5ms pulse: duty_u16 = (1.5 / 20.0) * 65535 = 4915
# Modify the duty_u16 value if the centre position is not safe for
# your application before connecting servos to the circuit.
SERVO_GP12 = PWM(Pin(SERVO_GP12_PIN), freq=50, duty_u16=4915)
SERVO_GP13 = PWM(Pin(SERVO_GP13_PIN), freq=50, duty_u16=4915)
SERVO_GP14 = PWM(Pin(SERVO_GP14_PIN), freq=50, duty_u16=4915)
SERVO_GP15 = PWM(Pin(SERVO_GP15_PIN), freq=50, duty_u16=4915)

SERVOS = (SERVO_GP12, SERVO_GP13, SERVO_GP14, SERVO_GP15)  # Tuple of all servo PWM outputs

def set_servo(servo, angle):
    # Set a servo to angle (0 to SERVO_RANGE degrees).
    # Pass the servo object as the first argument: set_servo(SERVO1, 45)
    angle = max(0, min(SERVO_RANGE, angle))
    pulse_us = SERVO_MIN_US + int(angle / SERVO_RANGE * (SERVO_MAX_US - SERVO_MIN_US))
    servo.duty_ns(pulse_us * 1000)
    return angle
import board
import neopixel
import time

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase

import adafruit_led_animation.color as color

# Works on Circuit Playground Express and Bluefruit.
# For other boards, change board.NEOPIXEL to match the pin to which the NeoPixels are attached.
pixel_pin = board.D18
# Change to match the number of pixels you have attached to your board.
num_pixels = 150

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, pixel_order=neopixel.RGB, brightness = 0.2, auto_write = False)
pixels.fill((0, 0, 0))

# anim = Blink(pixels, 0.5, color.PURPLE)
# anim = Sparkle(pixels, 0.05, (100, 100, 0), 10)
# anim = ColorCycle(pixels, 0.5, colors=[(100, 0, 0), (0, 100, 0), (0, 0, 100)])
# anim = Chase(pixels, 0.1, color=(0, 100, 0), size=3, spacing=10)
# anim = Comet(pixels, 0.1, (50, 50, 0))
# anim = Pulse(pixels, 0.1, (0, 50, 0))
# anim = SparklePulse(pixels, 0.05, (100, 100, 100))
# anim = Rainbow(pixels, 0.1)
anim = RainbowChase(pixels, 0.1, 3, 10)

while True:
    anim.animate()

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

from adafruit_led_animation.sequence import AnimationSequence

import adafruit_led_animation.color as color

import logging

class LedAnimations():
    def __init__(self, pin, num_pixels):
        # Works on Circuit Playground Express and Bluefruit.
        # For other boards, change board.NEOPIXEL to match the pin to which the NeoPixels are attached.
        self.pixel_pin = pin
        # Change to match the number of pixels you have attached to your board.
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels,
                pixel_order=neopixel.RGB, brightness = 0.2, auto_write = False)
        self.pixels.fill((0, 0, 0))

        sparkle = Sparkle(self.pixels, 0.05, (100, 100, 0), 10)
        color_cycle = ColorCycle(self.pixels, 0.5, colors=[(100, 0, 0), (0, 100, 0), (0, 0, 100)])
        chase = Chase(self.pixels, 0.1, color=(0, 100, 0), size=3, spacing=10)
        comet = Comet(self.pixels, 0.1, (50, 50, 0))
        pulse = Pulse(self.pixels, 0.1, (0, 50, 0))
        # sparkle = SparklePulse(self.pixels, 0.05, (100, 100, 100))
        rainbow = Rainbow(self.pixels, 0.1)
        blink = Blink(self.pixels, 0.5, color.PURPLE)
        rainbow_chase = RainbowChase(self.pixels, 0.1, 3, 10)

        self.anim_obj = AnimationSequence(
                sparkle,
                color_cycle,
                chase,
                comet,
                pulse,
                rainbow,
                blink,
                rainbow_chase,
                advance_interval=15)

    def next(self):
        self.anim_obj.next()

    def previous(self):
        self.anim_obj.previous()

    def animate(self):
        logging.debug("Calling animate()")
        self.anim_obj.animate()

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
        self.animation_state = "Play"

        self.pixel_pin = pin
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels,
                pixel_order=neopixel.RGB, brightness=0.1, auto_write=False)
        self.pixels.fill((0, 0, 0))

        sparkle1 = Sparkle(self.pixels, 0.04, (200, 200, 0), 10)
        sparkle2 = Sparkle(self.pixels, 0.04, (0, 200, 200), 10)
        color_cycle1 = ColorCycle(self.pixels, 1.5, colors=[(100, 0, 0), (0, 100, 0), (0, 0, 100)])
        color_cycle2 = ColorCycle(self.pixels, 1.5, colors=[(100, 50, 0), (200, 100, 0), (10, 220, 100)])
        chase1 = Chase(self.pixels, 0.04, color=(0, 200, 0), size=5, spacing=10)
        chase2 = Chase(self.pixels, 0.04, color=(200, 0, 0), size=5, spacing=30)
        comet1 = Comet(self.pixels, 0.04, (50, 50, 0))
        comet2 = Comet(self.pixels, 0.04, (150, 80, 100), reverse = True)
        pulse = Pulse(self.pixels, 0.04, (100, 150, 20))
        # sparkle = SparklePulse(self.pixels, 0.05, (100, 100, 100))
        rainbow = Rainbow(self.pixels, 0.04)
        blink = Blink(self.pixels, 0.5, (50, 0, 50))
        rainbow_chase = RainbowChase(self.pixels, 0.1, 3, 10)

        self.animation_array = [
                sparkle1, sparkle2,
                color_cycle1, color_cycle2,
                chase1, chase2,
                comet1, comet2,
                pulse,
                rainbow,
                blink,
                rainbow_chase
        ]
        self.anim_obj = AnimationSequence(*self.animation_array, random_order=True, advance_interval=20)

    def next(self):
        self.anim_obj.next()
        self.anim_obj._advance_interval = None
        # logging.info(self.anim_obj.current_animation)

    def previous(self):
        self.anim_obj.previous()
        self.anim_obj._advance_interval = None
        # logging.info(self.anim_obj.current_animation)

    def pause(self):
        self.anim_obj.freeze()
        self.animation_state = "Pause"

    def play(self):
        self.anim_obj.resume()
        self.animation_state = "Play"

    def random(self):
        self.anim_obj = AnimationSequence(*self.animation_array, random_order=True, advance_interval=20)
        self.anim_obj.random()

    def animate(self):
        logging.debug("Calling animate()")
        self.anim_obj.animate()

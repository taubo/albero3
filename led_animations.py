import board
import neopixel
import time
import sys

sys.path.append('/home/pi/albero3/animations')

import supermassive_rainbow
import function

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.group import AnimationGroup

from adafruit_led_animation.sequence import AnimationSequence

import adafruit_led_animation.color as color
import albero3_colors as col

import logging
from rainbowio import colorwheel

class LedAnimations():
    def __init__(self, pin, num_pixels):
        self.animation_state = "Play"

        self.pixel_pin = pin
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels,
                pixel_order=neopixel.GRB, brightness=0.15, auto_write=False)
        self.pixels.fill((0, 0, 0))

        sparkle1 = Sparkle(self.pixels, 0.04, (200, 200, 0), 10)
        sparkle2 = Sparkle(self.pixels, 0.04, (0, 200, 200), 10)
        sparkle3 = Sparkle(self.pixels, 0.04, col.GOLD, 20)

        color_cycle1 = ColorCycle(self.pixels, 1.5, colors=[(100, 0, 0), (0, 100, 0), (0, 0, 100)])
        color_cycle2 = ColorCycle(self.pixels, 1.5, colors=[col.TEAL, col.CYAN])
        color_cycle3 = ColorCycle(self.pixels, 1.5, colors=[col.MAGENTA, col.PURPLE])
        color_cycle4 = ColorCycle(self.pixels, 1.5, colors=[col.GOLD, col.ORANGE, col.AMBER])

        chase1 = Chase(self.pixels, 0.04, color=(0, 200, 0), size=5, spacing=10)
        chase2 = Chase(self.pixels, 0.04, color=(200, 0, 0), size=5, spacing=30)

        comet1 = Comet(self.pixels, 0.04, (50, 50, 0))
        comet2 = Comet(self.pixels, 0.04, (150, 80, 100), reverse = True)
        comet3 = Comet(self.pixels, 0.04, (0, 80, 200), reverse = True, tail_length=30)
        comet4 = Comet(self.pixels, 0.04, (200, 200, 0), reverse = True, tail_length=100)

        upper = PixelSubset(self.pixels, 75, 150)
        lower = PixelSubset(self.pixels, 0, 75)
        comet5 = Comet(lower, 0.04, col.RED, tail_length = 30)
        comet6 = Comet(upper, 0.04, col.RED, reverse = True, tail_length = 30)
        comet_crashing = AnimationGroup(comet5, comet6)

        pulse1 = Pulse(self.pixels, 0.01, (100, 150, 20))
        pulse2 = Pulse(self.pixels, 0.01, (100, 0, 220))
        pulse3 = Pulse(self.pixels, 0.01, (0, 100, 220))
        pulse4 = Pulse(self.pixels, 0.01, col.PURPLE)

        # sparkle = SparklePulse(self.pixels, 0.05, (100, 100, 100))
        rainbow = Rainbow(self.pixels, 0.04)
        blink = Blink(self.pixels, 0.5, (50, 0, 50))
        rainbow_chase1 = RainbowChase(self.pixels, 0.1, 3, 10)
        rainbow_chase2 = RainbowChase(self.pixels, 0.1, 10, 3)

        # questo puo' essere fatto usando PixelMap con l'animazione Rainbow
        supermassive_rainbow1 = supermassive_rainbow.SupermassiveRainbow(self.pixels, 0.1)

        sine1 = function.Sine(self.pixels, 0.04, col.GOLD)
        sine2 = function.Sine(self.pixels, 0.04, col.RED)
        sine3 = function.Sine(self.pixels, 0.04, col.GREEN)
        sine4 = function.Sine(self.pixels, 0.04, col.PURPLE, 2)
        sine5 = function.Sine(self.pixels, 0.04, col.ORANGE)
        sine6 = function.Sine(self.pixels, 0.04, col.PINK)

        self.animation_array = [
                sparkle1, sparkle2, sparkle3,
                color_cycle1, color_cycle2, color_cycle3, color_cycle4,
                chase1, chase2,
                comet1, comet2, comet3, comet4,
                comet_crashing,
                pulse1, pulse2, pulse3, pulse4,
                rainbow,
                blink,
                rainbow_chase1, rainbow_chase2,
                supermassive_rainbow1,
                sine1, sine2, sine3, sine4, sine5, sine6
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

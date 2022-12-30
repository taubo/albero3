from adafruit_led_animation.helper import PixelMap, PixelSubset
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.group import AnimationGroup

import board
import neopixel
import sys

sys.path.append('/home/pi/albero3/animations')
import stranger_things
import supermassive_rainbow
import function
import albero3_colors as col

pixels = neopixel.NeoPixel(board.D18, 150, brightness=0.2)

upper_side = PixelSubset(pixels, 75, 150)
lower_side = PixelSubset(pixels, 0, 75)
# upper_side.fill(col.GOLD)

animation1 = function.Sine(upper_side, 0.04, col.GOLD)
animation2 = function.Sine(lower_side, 0.04, col.PURPLE)
animation = AnimationGroup(animation1, animation2)
# animation = function.Sine(pixels, 0.04, col.GOLD)
# animation = Rainbow(upper_side, 0.04)
# animation = Blink(upper_side, 1.5, col.GOLD)

while True:
    animation.animate()

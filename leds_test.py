import board
import neopixel
import sys

sys.path.append('/home/pi/albero3/animations')
import stranger_things
import supermassive_rainbow
import function
import albero3_colors as col

pixels = neopixel.NeoPixel(board.D18, 150, brightness=0.2)

# anim = stranger_things.StrangerThings(pixels, 0.04, (0, 200, 0))
# anim = supermassive_rainbow.SupermassiveRainbow(pixels, 0.04)
anim = function.Sine(pixels, 0.04, col.GOLD)
# anim = function.Sine(pixels, 0.04, col.PURPLE)
# anim = function.Sync(pixels, 0.04, col.PURPLE, 4)

pixels.fill((0, 0, 0))
pixels.show()

while True:
    anim.animate()

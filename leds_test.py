import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 10)

pixels.fill((255, 0, 0))

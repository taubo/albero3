import board
import neopixel
import sys
import math

sys.path.append('/home/pi/albero3/animations')
import stranger_things
import supermassive_rainbow
import function
import pixel_shader
import albero3_colors as col

pixels = neopixel.NeoPixel(board.D18, 150, brightness=0.2)

def pixel_shader_example_function(context, now_s, pixel_index):
    return (200, 100, 50)

def pixel_shader_sine_example(context, now_s, pixel_index):
    if context is None:
        return (200, 100, 50)

    base_color = context
    frequency_hz = 1

    res_modulo = pixel_index % 5

    if res_modulo == 0:
        color_new = (
                int(function.sinize(base_color[0], now_s, frequency_hz / 2, pixel_index)),
                int(function.sinize(base_color[1], now_s, frequency_hz / 2, 2 * pixel_index)),
                int(function.sinize(base_color[2], now_s, frequency_hz / 2, 3 * pixel_index))
                )
    elif res_modulo == 2:
        color_new = (
                int(function.sinize(base_color[0], now_s, frequency_hz / 3, pixel_index)),
                int(function.sinize(base_color[1], now_s, frequency_hz / 3, pixel_index)),
                int(function.sinize(base_color[2], now_s, frequency_hz / 3, pixel_index))
                )
    else:
        color_new = (
                int(function.sinize(base_color[0], now_s, frequency_hz / 5, 3 * pixel_index)),
                int(function.sinize(base_color[1], now_s, frequency_hz / 5, 2 * pixel_index)),
                int(function.sinize(base_color[2], now_s, frequency_hz / 5, pixel_index))
                )

    return color_new

base_color = (200, 200, 200)
# anim = pixel_shader.PixelShader(pixels, 0.04, pixel_shader_example_function, None)
anim = pixel_shader.PixelShader(pixels, 0.04, pixel_shader.old_england_shader, base_color)

pixels.fill((0, 0, 0))
pixels.show()

while True:
    anim.animate()

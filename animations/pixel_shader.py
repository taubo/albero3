from adafruit_led_animation.animation import Animation
from time import monotonic_ns
import math

def sinize(val, t_s, f, phase):
    new_val = (val * (1 + math.sin(2 * math.pi * f * t_s + phase))) // 2
    return new_val

def old_england_shader(context, now_s, pixel_index):
    if context is None:
        return (200, 100, 50)

    base_color = context
    frequency_hz = 1

    res_modulo = pixel_index % 5

    if res_modulo == 0:
        color_new = (
                int(sinize(base_color[0], now_s, frequency_hz / 2, pixel_index)),
                int(sinize(base_color[1], now_s, frequency_hz / 2, 2 * pixel_index)),
                int(sinize(base_color[2], now_s, frequency_hz / 2, 3 * pixel_index))
                )
    elif res_modulo == 2:
        color_new = (
                int(sinize(base_color[0], now_s, frequency_hz / 3, pixel_index)),
                int(sinize(base_color[1], now_s, frequency_hz / 3, pixel_index)),
                int(sinize(base_color[2], now_s, frequency_hz / 3, pixel_index))
                )
    else:
        color_new = (
                int(sinize(base_color[0], now_s, frequency_hz / 5, 3 * pixel_index)),
                int(sinize(base_color[1], now_s, frequency_hz / 5, 2 * pixel_index)),
                int(sinize(base_color[2], now_s, frequency_hz / 5, pixel_index))
                )

    return color_new

class PixelShader(Animation):
    def __init__(self, pixel_object, speed, pixel_shader_function, context):
        super().__init__(pixel_object, speed, color=None, name=None)
        self.pixel_object = pixel_object
        self.speed = speed
        self.pixel_shader_function = pixel_shader_function
        self._context = context

    def set_context(self, context):
        self._context = context

    def draw(self):
        now_s = monotonic_ns() / 1000000000

        for pixel_index in range(0, len(self.pixel_object)):
            if self.pixel_shader_function is None:
                return;
            color_new = self.pixel_shader_function(self._context, now_s, pixel_index)
            self.pixel_object[pixel_index] = color_new

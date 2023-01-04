from adafruit_led_animation.animation import Animation
from time import monotonic_ns

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

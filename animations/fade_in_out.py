from adafruit_led_animation.animation import Animation
from time import monotonic_ns
import random

class FadeInOut(Animation):
    def __init__(self, pixel_object, speed, color, fade_time):
        super().__init__(pixel_object, speed, color, name=name)

        self.pixel_object = pixel_object
        self.speed = speed
        self.clor = color
        self.fade_time = fade_time
        self.notify_callback = []

    def add_listener(self, listener_callback):
        self.notify_callback.append(listener_callback)

    def draw(self):
        pass

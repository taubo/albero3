from adafruit_led_animation.animation import Animation
from rainbowio import colorwheel

class SupermassiveRainbow(Animation):
    def __init__(self, pixel_object, speed):
        super().__init__(pixel_object, speed, None, name=None)
        self.pixel_object = pixel_object
        self.index = 0

    def draw(self):
        self.index = (self.index + 1) % 256
        self.pixel_object.fill(colorwheel(self.index))

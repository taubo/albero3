from adafruit_led_animation.animation import Animation
from time import monotonic_ns
import math

def sinize(val, t_s, f, phase):
    new_val = (val * (1 + math.sin(2 * math.pi * f * t_s + phase))) // 2
    return new_val

class Sine(Animation):
    def __init__(self, pixel_object, speed, color, frequency_hz=1):
        super().__init__(pixel_object, speed, color, name=None)
        self.pixel_object = pixel_object
        self.color = color
        self.frequency_hz = frequency_hz

    def set_frequency_hz(self, frequency_hz):
        self.frequency_hz = frequency_hz

    def draw(self):
        now_s = monotonic_ns() / 1000000000
        for index in range(0, len(self.pixel_object)):
            color_new = (
                    int(self.sinize(self.color[0], now_s, self.frequency_hz, index)),
                    int(self.sinize(self.color[1], now_s, self.frequency_hz, index)),
                    int(self.sinize(self.color[2], now_s, self.frequency_hz, index)))
            self.pixel_object[index] = color_new

    def sinize(self, val, t_s, f, phase):
        new_val = (val * (1 + math.sin(2 * math.pi * f * t_s + phase))) // 2
        return new_val

# al momento non mi piace
class Sync(Animation):
    def __init__(self, pixel_object, speed, color, period_s=1):
        super().__init__(pixel_object, speed, color, name=None)
        self.pixel_object = pixel_object
        self.color = color
        self.period_s = period_s
        self.start_delay = monotonic_ns() / 1000000000

    def draw(self):
        now_s = monotonic_ns() / 1000000000
        for index in range(1, len(self.pixel_object)):
            color_new = (
                    int(self.color[0] * self.sync_func(now_s, self.period_s, self.start_delay + index / 10) ** 2),
                    int(self.color[1] * self.sync_func(now_s, self.period_s, self.start_delay + index / 10) ** 2),
                    int(self.color[2] * self.sync_func(now_s, self.period_s, self.start_delay + index / 10) ** 2),
                    )
            self.pixel_object[index] = color_new
        # print(self.color[1] * self.sync_func(now_s, self.period_s, 0))
        # print(f"{now_s=} -- {color_new=}")
        # self.pixel_object.fill(color_new)

    def sync_func(self, t_s, period_s, delay_s):
        x = math.pi * (t_s - delay_s) / period_s
        return math.sin(x) / x

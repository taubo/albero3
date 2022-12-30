from adafruit_led_animation.animation import Animation
from adafruit_led_animation.helper import pulse_generator
from time import monotonic_ns
import random

class StrangerThings(Animation):
    def __init__(self, pixel_object, speed, color, period_s=3, number_of_strangers=50):
        super().__init__(pixel_object, speed, color, name=None)
        self.selected_pixels_indexes = []
        self.interval_between_selections_ms = 3000
        self.last_selection_time_ms = 0
        self.last_update_list_ms = 0

        self.pixel_object = pixel_object
        self.speed = speed
        # self.color = color
        self.period_ms = period_s * 1000
        self.number_of_strangers = number_of_strangers

        self.pulse_generators = [pulse_generator(period_s, self) for i in range(0, len(self.pixel_object))]

        random.seed()

    def draw(self):
        now_ms = monotonic_ns() // 1000
        if len(self.selected_pixels_indexes) < self.number_of_strangers:
            if now_ms - self.last_selection_time_ms >= self.interval_between_selections_ms:
                new_index = random.randint(0, len(self.pixel_object) - 1)
                self.selected_pixels_indexes.append(new_index)
                self.last_selection_time_ms = now_ms
        else:
            if now_ms - self.last_update_list_ms >= self.period_ms:
                idx = self.selected_pixels_indexes.pop(0)
                self.pixel_object[idx] = (0, 0, 0)
                self.last_update_list_ms = now_ms

        for pixel_idx in self.selected_pixels_indexes:
            color = next(self.pulse_generators[pixel_idx])
            self.pixel_object[pixel_idx] = color


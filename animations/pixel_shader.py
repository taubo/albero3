class PixelShader(Animation):
    def __init__(self, pixel_object, speed, pixel_shader_function):
        super()__init__(pixel_object, speed, color=None, name=None)
        self.pixel_object = pixel_object
        self.speed = speed
        self.pixel_shader_function = pixel_shader_function

    # def draw(self):
    #     now_s = monotonic_ns() / 1000000000
    #     for index in 

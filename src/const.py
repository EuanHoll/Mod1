

S_WIDTH = 1280
S_HEIGHT = 720
S_RATIO = S_WIDTH/S_HEIGHT
MAX_HEIGHT = 20


class WaterSim:
    def __init__(self):
        self.raining = False
        self.const_wave = False
        self.rising = False
        self.last_rain = 0
        self.last_rise = 0
        self.layer = 0

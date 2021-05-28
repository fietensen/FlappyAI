class Agent:
    def __init__(self, screen_resolution):
        self.resolution = screen_resolution
        self.fitness = 0
        self.dead = False
        self.screen = None
        self.y = screen_resolution[1]//2
        self.rect = ((10, self.y), (self.resolution[0]//20, self.resolution[0]//25))
        self.vvelocity = 0

    def copyview(self, surface_array):
        self.screen = surface_array

    def jump(self):
        self.vvelocity = 3.6

    def move(self):

        self.vvelocity -= .08
        self.y -= 1*self.vvelocity
        self.rect = ((10, self.y), (self.resolution[0]//20, self.resolution[1]//20))

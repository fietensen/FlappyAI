from pygame import Rect, draw
import numpy as np

class PolesObject:
    def __init__(self, screen_resolution):
        self.resolution = screen_resolution
        self.x = screen_resolution[0]
        self.width = self.resolution[0]//10
        self.height = np.random.uniform(30, self.resolution[1]-self.resolution[1]//3)
        self.gapsize = screen_resolution[0]//6

    def move(self):
        self.x -= 2

    def display(self, screen):

        upper_rect = Rect((self.x, 0), (self.width, self.height))
        lower_rect = Rect(
                (self.x, self.height+self.gapsize),
                (self.width, self.resolution[1] - self.height+self.gapsize))

        draw.rect(screen, (25,255,25), upper_rect)
        draw.rect(screen, (25,255,25), lower_rect)


from game.pole import PolesObject
from game.agent import Agent
from pygame import Rect
import pygame, struct
import numpy as np

class Game:
    def __init__(self, resolution):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(resolution) # init window
        self.playerpos = (0, resolution[1]) # initial player position
        self.poles = []
        self.poles.append(PolesObject(resolution))
        self.agents = []
        self.birdimg = pygame.image.load("graphics/flappybird.png")
        self.birdimg = pygame.transform.scale(self.birdimg, (resolution[0]//20, resolution[0]//25))

    def step(self):
        self.screen.fill((51,255,255))
        remove_poles = []
        for index, pole in enumerate(self.poles):
            if pole.x+pole.width < 0:
                remove_poles.append(index)
            else:
                pole.move()
                pole.display(self.screen)

        for remove_pole in remove_poles:
            self.poles.pop(remove_pole)

        if self.poles[-1].x+self.poles[-1].width < self.resolution[0]-np.random.uniform(
                self.resolution[0]//3,
                self.resolution[0]//2):
            self.poles.append(PolesObject(self.resolution))

        #view = pygame.surfarray.array2d(self.screen)&0xFF
        for agent in self.agents:
            agent.move()
            for pole in self.poles:
                pole_upper = Rect((pole.x, 0), (pole.width, pole.height))
                pole_lower = Rect((pole.x, pole.height+pole.gapsize),
                        (pole.width, pole.resolution[1] - pole.height+pole.gapsize))

                if Rect(agent.rect).colliderect(pole_upper) or Rect(agent.rect).colliderect(pole_lower):
                    agent.dead = True
                elif agent.y < 0 or agent.y > self.resolution[1]:
                    agent.dead = True
                elif not agent.dead:
                    agent.fitness += .001
                    self.screen.blit(self.birdimg, agent.rect)

        pygame.display.flip()

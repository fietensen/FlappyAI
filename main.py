from game.game import Game
from game.agent import Agent
from game import quit
from pygame.time import Clock
from geneticagent import AgentANN, EvolveAgents, GetFittest
import pygame
import random, sys, os
import numpy as np

mutationrate = 0.2
n_agents = 50
resolution = (600,480)
game = Game(resolution)



generation = 0
agents = []

for i in range(n_agents):
    a = Agent(resolution)
    aANN = AgentANN(resolution)
    game.agents.append(a)
    agents.append((a, aANN))

#test_agent = Agent(resolution)
#game.agents.append(test_agent)
#agents.append((test_agent, None))
running = True
gameclock = Clock()

tickspeed = 120

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("tickspeed {} -> {}".format(tickspeed, tickspeed+10))
                tickspeed += 10
            elif event.key == pygame.K_DOWN:
                print("tickspeed {} -> {}".format(tickspeed, tickspeed-10))
                tickspeed -= 10
            #elif event.key == pygame.K_SPACE:
            #    test_agent.jump()

    gameclock.tick(tickspeed)#resolution[0]//5)

    game.step()


    living_agents = 0

    for agent, agentnetwork in agents:
        if not agent.dead:
            living_agents += 1
            if agentnetwork.decide(np.array([agent.y, game.poles[0].height, game.poles[0].height+game.poles[0].gapsize])): #agent.screen.reshape(resolution[0]*resolution[1],) / 255):
                agent.jump()

    if living_agents == 0:
        #game = Game(resolution)
        #test_agent = Agent(resolution)
        #game.agents.append(test_agent)
        #agents = [(test_agent, None)]

        fittest = GetFittest(agents, n=1, network=False)
        print("Ended generation {} fittest indivdual: {}".format(generation, fittest[0].fitness))
        agents = EvolveAgents(agents, Agent, resolution, mutationrate, n_agents)
        game = Game(resolution)
        for agent, agentnetwork in agents:
            game.agents.append(agent)
        generation += 1
        print("Started generation {}".format(generation))
quit()

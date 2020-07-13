from geneticagent.neuralnetwork import AgentANN
from random import randint
import numpy as np

def MapMatrix(mid, matrix, function):
    for r_index, row in enumerate(matrix):
        for c_index, column in enumerate(row):
            matrix[r_index,c_index] = function(mid, r_index, c_index)

def CrossBreed(parent1, parent2, mutationrate, resolution):
    network = AgentANN(resolution, child=True)

    def inherit(mid, row, column):
        mutate = np.random.random() < mutationrate
        parent = parent1 if randint(0,1) else parent2
        if mid == 0:
            return np.random.randn() if mutate else parent.hidden1_weights[row,column]
        elif mid == 1:
            return np.random.randn() if mutate else parent.hidden2_weights[row,column]
        elif mid == 2:
            return np.random.randn() if mutate else parent.output_weights[row,column]

    MapMatrix(0, network.hidden1_weights, inherit)
    MapMatrix(1, network.hidden2_weights, inherit)
    MapMatrix(2, network.output_weights, inherit)
    return network

def GetFittest(agents, n=2, network=True):
    fit = []
    fitnesses = []
    for gameagent, networkagent in agents:
        fitnesses.append(gameagent.fitness)

    for i in range(n):
        max_fitness = max(fitnesses)
        idx = fitnesses.index(max_fitness)
        fitnesses.pop(idx)
        fit.append(agents.pop(idx)[network])

    return fit

def EvolveAgents(agents, Agent, resolution, mutationrate, gensize):
    fittest_agents = GetFittest(agents)
    new_agents = []
    for i in range(gensize-2):
        game_agent = Agent(resolution)
        network_agent = CrossBreed(*fittest_agents, mutationrate, resolution)
        new_agents.append((game_agent, network_agent))

    new_agents += zip([Agent(resolution)]*2, fittest_agents)
    return new_agents

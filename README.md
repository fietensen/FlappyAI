# FlappyAI

## What is this?
FlappyAI is an implementation of an [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) combined with a [Feedforward Neural Network](https://en.wikipedia.org/wiki/Feedforward_neural_network).  
In machine learning, this is known as [Neuroevolution](https://en.wikipedia.org/wiki/Neuroevolution).  
This program provides a simplistic clone of the popular mobile game "Flappy Bird" by Dong Nguyen  
and a population of 50 Game Agents. At the beginning these Agents will  
most likely fail to even pass one of the pipes, but as time passes by  
the future generations of the population will get better and better at playing the game.  

## How do I set it up?
Installing is easy, you need Python3 which can be obtained from https://python.org and the packet manager PIP.  
In order to install the dependencies, open a terminal and navigate to your installation folder.  
Then you can install the program's dependencies with `pip install -r requirements.txt`  
now all you have to do is to execute the `main.py` script located at the in root folder of the project.  

This has been tested on Arch Linux using Python 3.8.3, PIP 20.0.2,  
numpy 1.18.5 and pygame 1.9.6
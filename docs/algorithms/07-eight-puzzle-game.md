# A* Search for the 8-puzzle game

This excercise generates and solves the 8-number jigsaw puzzle.  It is using the A* algorithm and leverages 4 different evaluation methods

## Required packages

Install the following packages, with pip3 install

- random: used to randomly generate (test)data
- matplotlib.pyplot: used for plotting
- timeit: used to time the execution of the different solving methods
- math: used for sqrt
- unittest: used for the unit tests 
- numpy: used for some array operations

## Source files description

__Priority Queue__: [priority_queue.py](../src/algorithms/07-eight-puzzle-game/priority_queue.py)

In this file, I've made an implementation of a priority queue with peek/lock capabilities that sorts (and pops) messages based on the priority they get tagged with

__Puzzle__: [puzzle.py](../src/algorithms/07-eight-puzzle-game/puzzle.py)

This file contains all methods and implementations to calculate moves, simulate moves and render the game board

__Jigsaw__: [jigsaw.py](../src/algorithms/07-eight-puzzle-game/jigsaw.py)

Contains the implementation for the A* algorithm and has an implementation to time and plot the different evaluation methods
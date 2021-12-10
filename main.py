from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    for map_index in [2, 3, 4, 5]:
        shorter_robot_heuristic_experiment(map_index)

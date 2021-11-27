from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


import AutomaticGenerator


if __name__ == "__main__":
    w_experiment(0)
    w_experiment(1)
    w_experiment(2)
    test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)
    test_robot(WAStartRobot, [99], heuristic=center_manhattan_heuristic)

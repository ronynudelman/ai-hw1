from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    #a = solve_and_display(WAStartRobot, 4, blit=False, heuristic=center_manhattan_heuristic)
    #a = solve_and_display(WAStartRobot, 4, blit=False, heuristic=ShorterRobotHeuristic, k=8)
    #for k in [2, 4, 6, 8]:
    #    test_robot(WAStartRobot, [3, 4], heuristic=ShorterRobotHeuristic, k=k)
    #test_robot(WAStartRobot, [3, 4], heuristic=center_manhattan_heuristic)
    for index in [3]:
        shorter_robot_heuristic_experiment(index)
from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


TITLE = 60
END = 126


def q4_2():
    print('*' * TITLE, "q4_2", '*' * TITLE)
    test_robot(BreadthFirstSearchRobot, [0, 1, 2, 3, 4, 5])
    print('*' * END)
    print()


def q5_3():
    print('*' * TITLE, "q5_3", '*' * TITLE)
    test_robot(UniformCostSearchRobot, [0, 1, 2, 3, 4, 5])
    print('*' * END)
    print()


def q7_3():
    print('*' * TITLE, "q7_3", '*' * TITLE)
    test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=tail_manhattan_heuristic)
    print('*' * END)
    print()


def q8_2():
    print('*' * TITLE, "q8_2", '*' * TITLE)
    test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)
    test_robot(WAStartRobot, [99], heuristic=center_manhattan_heuristic)
    print('*' * END)
    print()


def q10_2():
    print('*' * TITLE, "q10_2", '*' * TITLE)
    for maze_index in [0, 1, 2]:
        w_experiment(maze_index)
    print('*' * END)
    print()


def q16_1():
    print('*' * TITLE, "q16_1", '*' * TITLE)
    for k in [2, 4, 6, 8]:
        test_robot(WAStartRobot, [3, 4], heuristic=ShorterRobotHeuristic, k=k)
    print('*' * END)
    print()


def q16_4():
    print('*' * TITLE, "q16_4", '*' * TITLE)
    for maze_index in [2, 3, 4, 5]:
        shorter_robot_heuristic_experiment(maze_index)
    print('*' * END)
    print()


def main():
    q4_2()
    q5_3()
    q7_3()
    q8_2()
    q10_2()
    q16_1()
    q16_4()

if __name__ == "__main__":
    main()

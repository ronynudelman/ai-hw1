from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


import AutomaticGenerator


if __name__ == "__main__":
    AutomaticGenerator.prepare_csv_file()
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=tail_manhattan_heuristic)
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=center_manhattan_heuristic)
    test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)
    test_robot(WAStartRobot, [99], heuristic=center_manhattan_heuristic)

    # test_robot(UniformCostSearchRobot, [0, 1, 2, 3, 4, 5])
    # test_robot(BreadthFirstSearchRobot, [0, 1, 2, 3, 4, 5])
    # solve_and_display(BreadthFirstSearchRobot, 5)
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=center_manhattan_heuristic)
    # for i in range(6):
    #     w_experiment(i)
    #     print(f"done {i}", flush=True)
    # print("with simple heuristic:")
    # test_robot(WAStartRobot, [3], heuristic=center_manhattan_heuristic)
    # print("with complicated heuristic:")
    # maze_problem = create_problem("maze_3")
    # h = ShorterRobotHeuristic(maze_problem, k=2)
    # test_robot(WAStartRobot, [3], heuristic=h)

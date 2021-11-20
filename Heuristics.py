import numpy as np
from MazeProblem import MazeState, MazeProblem, compute_robot_direction
from Robot import UniformCostSearchRobot
from GraphSearch import NodesCollection


def tail_manhattan_heuristic(state: MazeState):
    # TODO (EX 7.2), implement heuristic, delete exception
    tails_manhattan_dist = np.sum(np.abs(state.tail - state.maze_problem.tail_goal))
    return state.maze_problem.forward_cost * tails_manhattan_dist


def center_manhattan_heuristic(state: MazeState):
    # TODO (EX 9.2), implement heuristic, delete exception
    current_robot_center = (state.head + state.tail) / 2
    goal_center = (state.maze_problem.head_goal + state.maze_problem.tail_goal) / 2
    return np.sum(np.abs(current_robot_center - goal_center))

class ShorterRobotHeuristic:
    def __init__(self, maze_problem: MazeProblem, k):
        assert k % 2 == 0, "odd must be even"
        assert maze_problem.length - k >= 3, f"it is not possible to shorten a {maze_problem.length}-length robot by " \
                                             f"{k} units because robot length has to at least 3"
        self.k = k
        ################################################################################################################
        # TODO (EX. 13.2): replace all three dots, delete exception
        shorter_robot_head_goal, shorter_robot_tail_goal = self._compute_shorter_head_and_tails(maze_problem.head_goal,
                                                                                           maze_problem.tail_goal)
        self.new_maze_problem = MazeProblem(maze_map=maze_problem.maze_map,
                                            initial_head=shorter_robot_tail_goal,
                                            initial_tail=shorter_robot_head_goal,
                                            head_goal=shorter_robot_head_goal,  # doesn't matter, don't change
                                            tail_goal=shorter_robot_tail_goal)  # doesn't matter, don't change
        self.node_dists = UniformCostSearchRobot().solve(self.new_maze_problem, compute_all_dists=True)
        ################################################################################################################

        assert isinstance(self.node_dists, NodesCollection)

    def _compute_shorter_head_and_tails(self, head, tail):
        # TODO (EX. 13.1): complete code here, delete exception
        robot_direction = compute_robot_direction(head, tail)
        shorter_head = head - (self.k / 2) * robot_direction
        shorter_tail = tail + (self.k / 2) * robot_direction
        return shorter_head, shorter_tail

    def __call__(self, state: MazeState):
        # TODO (EX. 13.3): replace each three dots, delete exception
        shorter_head_location, shorter_tail_location = _compute_shorter_head_and_tails(state.head,
                                                                                       state.tail)
        new_state = MazeState(self.new_maze_problem,
                              head=shorter_head_location,
                              tail=shorter_tail_location)
        if new_state in self.node_dists:
            node = self.node_dists.get_node(new_state)
            return node.g_value
        else:
            return center_manhattan_heuristic(state)  # what should we return in this case,
                                                      # so that the heuristic would be as
                                                      # informative as possible
                                                      # but still admissible

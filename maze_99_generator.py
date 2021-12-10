import math


MAP_SIZE = 250
ROBOT_LENGTH = MAP_SIZE // 5 - 1
assert ROBOT_LENGTH % 2 == 1
COLUMN = MAP_SIZE // 2
START_TAIL_ROW = math.floor(MAP_SIZE - ROBOT_LENGTH * 1.2)
MAZE_99_PATH = "Mazes/maze_99.csv"

START_TAIL = [START_TAIL_ROW, COLUMN]
START_HEAD = [START_TAIL_ROW - ROBOT_LENGTH + 1, COLUMN]
GOAL_TAIL = [START_HEAD[0] - 1, COLUMN]
GOAL_HEAD = [START_TAIL[0] - 1, COLUMN]

with open(MAZE_99_PATH, 'w') as f:
    for i in range(MAP_SIZE):
        current_line = ""
        for j in range(MAP_SIZE - 1):
            if [i, j] == START_TAIL:
                current_line += "1.0,"
            elif [i, j] == START_HEAD:
                current_line += "2.0,"
            elif [i, j] == GOAL_TAIL:
                current_line += "3.0,"
            elif [i, j] == GOAL_HEAD:
                current_line += "4.0,"
            else:
                current_line += "0.0,"
        current_line += "0.0\n"
        f.write(current_line)

# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]

grid2 = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    closed_list = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_list[goal[0]][goal[1]] = 0
    path_list = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    path_list[goal[0]][goal[1]] = '*'
    x = goal[0]
    y = goal[1]
    v = 0
    open_list = [[v, x, y]]

    resign = False
    while not resign:
        if len(open_list) == 0:
            resign = True
            #print('resigning')
        else:
            open_list.sort(reverse=True)
            next_item = open_list.pop()
            x = next_item[1]
            y = next_item[2]
            v = next_item[0]

        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]

            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                if closed_list[x2][y2] == 99 and grid[x2][y2] == 0:
                    v2 = v + cost
                    open_list.append([v2, x2, y2])
                    closed_list[x2][y2] = v2
                    path_list[x2][y2] = delta_name[(i-2)%4]


    value = closed_list
    policy = path_list
    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return policy

A = compute_value(grid,goal,cost)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid2 = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

grid = [[0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    closed_list = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    closed_list[init[0]][init[1]] = 1
    expand_list = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand_list[init[0]][init[1]] = 0
    expand_list_prev = expand_list[init[0]][init[1]]
    #expand
    x = init[0]
    y = init[1]
    g = 0
    open_list = [[g, x, y]]  # initial open list [cost, x, y]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in expand_list]))

    found = False
    resign = False

    while found is False and resign is False:
        if len(open_list) == 0:
            resign = True
            #print('fail')
        else:
            open_list.sort(reverse=True)
            print(open_list)
            next_item = open_list.pop()
            x = next_item[1]
            y = next_item[2]
            g = next_item[0]
            #print('take item', next_item)
            #print(open_list)

            if x == goal[0] and y == goal[1]:
                found = True
                print('goal is', next_item)
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed_list[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open_list.append([g2, x2, y2])
                            closed_list[x2][y2] = 1
                            expand_list[x2][y2] = expand_list_prev + 1
                            expand_list_prev = expand_list[x2][y2]
                            #print(g2,x2,y2)
    path = next_item

    #print(closed_list)
    return expand_list


A = search(grid,init,goal,cost)
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in A]))
A = search(grid2,init,goal,cost)
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in A]))
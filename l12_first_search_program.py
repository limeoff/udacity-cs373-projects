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

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    open_list = []
    closed_list = []
    open_list.append([0] + init)  # initial open list [cost, x, y]
    #expand
    print(open_list)
    c = 0

    for i in range(len(open_list)):

        take_list_item = open_list[i]
        open_list.remove(open_list[i])
        closed_list.append(i)
        c += 1
        new_open_list = []
        for d in delta:
            row = take_list_item[1]+d[0]
            col = take_list_item[2]+d[1]

            if grid[row][col] == 0 and (row >= 0) and (col >= 0):
                new_open_list.append([c, row, col])
                #print(grid[(take_list_item[1]+d[0])][(take_list_item[2]+d[1])])

        #open_list = new_open_list

        print(open_list)

    #gValue


    #take list

    path=grid[init[0]][init[1]]


    return path

search(grid,init,goal,cost)
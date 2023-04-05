import copy

river_list = {}  # keeps track of rivers we have detected and their co-ordinates
river = 1
river_coordinates = []


def solution(mat):
    global river
    global river_coordinates
    global matrix
    global traced_matrix
    matrix = mat
    traced_matrix = copy.deepcopy(mat)
    for row in range(matrix.__len__())[:]:
        for col in range(matrix[row].__len__())[:]:
            if matrix[row][col] != 0:
                if not move(row, col):
                    pass
                river += 1
                river_coordinates = []
    for stream in river_list:
        if river_list[stream].__len__() == 0:
            continue
        print(river_list[stream], river_list[stream].__len__())


# Scans the surrounding cells to check if any cell is '1'
def pathfinder(x_axis, y_axis):
    if x_axis + 1 == matrix.__len__():
        x_axis = -1
    if y_axis + 1 == matrix[x_axis].__len__():
        y_axis = -1

    path_array = {'north': matrix[x_axis - 1][y_axis], 'south': matrix[x_axis + 1][y_axis],
                  'east': matrix[x_axis][y_axis + 1], 'west': matrix[x_axis][y_axis - 1],
                  'northeast': matrix[x_axis - 1][y_axis + 1], 'northwest': matrix[x_axis - 1][y_axis - 1],
                  'southeast': matrix[x_axis + 1][y_axis + 1], 'southwest': matrix[x_axis + 1][y_axis - 1]}
    return path_array


# check to make sure that the next move isn't to a cell that has already been traced
def is_next_move_allowed(x, y, p_move):
    if x == traced_matrix.__len__():
        x = -1
    if y == traced_matrix[x].__len__():
        y = -1
    return not (traced_matrix[x][y] == 'x')


def add_cell_to_river(cell_x, cell_y):
    if traced_matrix[cell_x][cell_y] != 'x':
        river_coordinates.append(str(cell_x) + ',' + str(cell_y))
    river_list[river] = river_coordinates


# Moves the current cell to the next one based on the results of 'pathfinder()'
def move(move_x, move_y):
    if move_x == traced_matrix.__len__():
        move_x = -1
    elif move_y == traced_matrix[move_x].__len__():
        move_y = -1

    add_cell_to_river(move_x, move_y)
    traced_matrix[move_x][move_y] = 'x'
    cur_pos = {'x': move_x, 'y': move_y}
    path = pathfinder(move_x, move_y)
    for step in path:
        if (path[step] == 1) & (step == 'north') & is_next_move_allowed(move_x - 1, move_y, cur_pos):
            move(move_x - 1, move_y)
        if (path[step] == 1) & (step == 'south') & is_next_move_allowed(move_x + 1, move_y, cur_pos):
            move(move_x + 1, move_y)
        if (path[step] == 1) & (step == 'east') & is_next_move_allowed(move_x, move_y + 1, cur_pos):
            move(move_x, move_y + 1)
        if (path[step] == 1) & (step == 'west') & is_next_move_allowed(move_x, move_y - 1, cur_pos):
            move(move_x, move_y - 1)
        if (path[step] == 1) & (step == 'northeast') & is_next_move_allowed(move_x - 1, move_y + 1, cur_pos):
            move(move_x - 1, move_y + 1)
        if (path[step] == 1) & (step == 'northwest') & is_next_move_allowed(move_x + 1, move_y, cur_pos):
            move(move_x - 1, move_y - 1)
        if (path[step] == 1) & (step == 'southeast') & is_next_move_allowed(move_x + 1, move_y + 1, cur_pos):
            move(move_x + 1, move_y + 1)
        if (path[step] == 1) & (step == 'southwest') & is_next_move_allowed(move_x + 1, move_y - 1, cur_pos):
            move(move_x + 1, move_y - 1)

    return True


solution([
[1, 0, 0],
[0, 0, 0],
[0, 0, 1]
])

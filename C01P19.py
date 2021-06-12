from collections import OrderedDict
from copy import deepcopy

cinema_layout = [
    '..*...*.**',
    '.....**...',
    '*.*...*..*',
    '.**....*.*',
    '...*..*.*.',
    '*......*.*',
    '.***...*..',
    '.....**..*',
    '..*.*.*..*',
    '***.*.**..'
]
friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]


def get_persons_positions(data):
    start_element = data[0]
    positions = OrderedDict()
    positions[start_element] = [0, 0]

    for i in range(1, len(data)):
        element = data[i][0]
        position = data[i][1]
        if i == 1:
            from_element = start_element
        else:
            from_element = data[i][2]

        if position == 'A':
            positions[element] = [positions[from_element][0] - 1, positions[from_element][1]]

        elif position == 'R':
            positions[element] = [positions[from_element][0], positions[from_element][1] + 1]

        elif position == 'L':
            positions[element] = [positions[from_element][0], positions[from_element][1] - 1]

        elif position == 'D':
            positions[element] = [positions[from_element][0] + 1 , positions[from_element][1]]

    return positions


def in_matrix(r, c, m):
    return 0 <= r < len(m) and 0 <= c <= len(m[0])


def stranger_forms(cinema_layout, friends_configuration):
    possible_placement = []
    cinema_layout_to_list = [list(el) for el in cinema_layout]
    grid = get_persons_positions(friends_configuration)
    count = 0

    for r in range(len(cinema_layout_to_list)):
        for c in range(len(cinema_layout_to_list[0])):
            new_copy = deepcopy(cinema_layout_to_list)
            for k, v in grid.items():
                count += 1
                row, col = v
                new_r = r + row
                new_c = c + col

                if not in_matrix(new_r, new_c, new_copy) or new_copy[new_r][new_c] != '.':
                    count = 0
                    break

                new_copy[new_r][new_c] = k
                if count == len(grid):
                    result = [''.join(el) for el in new_copy]
                    possible_placement.append(result)

    return possible_placement


print('\n'.join(['\n'.join(el) for el in stranger_forms(cinema_layout, friends_configuration)]))
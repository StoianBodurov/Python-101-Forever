def in_matrix(matrix, position):
    r, c = position

    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])


def sum_matrix(matrix, start_position):
    row, col = start_position
    bomb_power = matrix[row][col]
    matrix_sum = sum(sum(r) for r in matrix)
    positions = [(0, -1), (0, 1), (-1, 0), (1, 0), ( -1, -1),  (1, -1), (-1, 1), (1, 1)]

    for el in positions:
        r, c = el
        new_row = row + r
        new_col = col + c
        if in_matrix(matrix, (new_row, new_col)):
            value = matrix[new_row][new_col]
            new_value = value - bomb_power
            if new_value < 0:
                new_value = 0
            matrix_sum -= value - new_value

    return matrix_sum


def matrix_bombing_plan(m):
    result ={}
    for r in range(len(m)):
        for c in range(len(m[r])):
            position = r, c
            result[position] = sum_matrix(m, position)

    return result
def count_matches(s, w):
    if w == w[:: -1]:
        return s.count(w)

    return s.count(w) + s[:: -1].count(w)


def horizontal_match(m, w):
    count = 0
    for row in m:
        new_word = ''.join(row)
        count += count_matches(new_word, w)

    return count


def vertical_match(m, w):
    count = 0

    for c in range(len(m[0])):
        new_word = ''
        for r in range(len(m)):
            new_word += m[r][c]
        count += count_matches(new_word, w)
    return count


def left_diagonals_match(m, w):
    count = 0

    for c in range(len(m[0])):
        new_word = ''
        row = 0
        column = c
        while row < len(m) and column < len(m[0]):
            new_word += m[row][column]
            row += 1
            column += 1
        count += count_matches(new_word, w)

    for r in range(1, len(m)):
        new_word = ''
        row = r
        column = 0
        while row < len(m) and column < len(m[0]):
            new_word += m[row][column]
            row += 1
            column += 1
        count += count_matches(new_word, w)

    return count


def right_diagonals_match(m, w):
    count = 0

    for c in range(len(m[0]) - 1, -1, -1):
        new_word = ''
        row = 0
        column = c
        while row < len(m) and column >= 0:
            new_word += m[row][column]
            row += 1
            column -= 1
        count += count_matches(new_word, w)

    for r in range(1, len(m)):
        new_word = ''
        row = r
        column = len(m[r]) - 1
        while row < len(m) and column >= 0:
            new_word += m[row][column]
            row += 1
            column -= 1
        count += count_matches(new_word, w)

    return count


def word_counter(m, w):
    return horizontal_match(m, w) + vertical_match(m, w) + \
           left_diagonals_match(m, w) + right_diagonals_match(m, w)
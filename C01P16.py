def lower_or_upper_letter(letter, upper_condition):
    if upper_condition:
        return letter.upper()

    return letter


def message_to_numbers(message):
    el = message[0]
    is_upper = False
    counter = 0
    result = ''
    mapper = {0: [' '],
              2: ['a', 'b', 'c'],
              3: ['d', 'e', 'f'],
              4: ['g', 'h', 'i'],
              5: ['j', 'k', 'l'],
              6: ['m', 'n', 'o'],
              7: ['p', 'q', 'r', 's'],
              8: ['t', 'u', 'v'],
              9: ['w', 'x', 'y', 'z']}

    for index in range(1, len(message)):
        next_el = message[index]
        if el == 1:
            is_upper = True
        if el in mapper:
            if el == next_el:
                counter += 1
                if counter == len(mapper[el]):
                    counter = 0

            else:
                result += lower_or_upper_letter(mapper[el][counter], is_upper)
                counter = 0
                is_upper = False

        el = next_el
        if index == len(message) - 1:
            result += lower_or_upper_letter(mapper[el][counter], is_upper)
    return result
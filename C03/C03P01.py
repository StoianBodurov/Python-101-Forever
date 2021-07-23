class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened

    def is_inside(self, value):
        start = self.start
        end = self.end
        if self.start_opened is True:
            start += 1

        if self.end_opened is True:
            end -= 1

        return start <= value <= end

    def stringify(self):
        start_symbol = '['
        end_symbol = ']'
        if self.start_opened is True:
            start_symbol = '('

        if self.end_opened is True:
            end_symbol = ')'

        return f'{start_symbol}{self.start}, {self.end}{end_symbol}'
#
#
# closed_interval = Interval(1, 10)
#
# result = [closed_interval.is_inside(1) is True,
#           closed_interval.is_inside(5) is True,
#           closed_interval.is_inside(10) is True,
#
#           closed_interval.stringify() == "[1, 10]", ]
#
# for r in result:
#     print(r)
#
# closed_interval = Interval(1, 10, start_opened=True, end_opened=True)
#
# result_1 = [closed_interval.is_inside(1) is False,
#             closed_interval.is_inside(5) is True,
#             closed_interval.is_inside(10) is False,
#
#             closed_interval.stringify() == "(1, 10)", ]
#
# for r in result_1:
#     print(r)
#
# half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)
#
# result_2 = [half_opened_interval.is_inside(1) is True,
#             half_opened_interval.is_inside(5) is True,
#             half_opened_interval.is_inside(10) is False,
#
#             half_opened_interval.stringify() == "[1, 10)", ]
#
# for r in result_2:
#     print(r)
#
# half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)
#
# result_3 = [half_opened_interval.is_inside(1) is False,
#             half_opened_interval.is_inside(5) is True,
#             half_opened_interval.is_inside(10) is True,
#
#             half_opened_interval.stringify() == "(1, 10]", ]
#
#
# for r in result_3:
#     print(r)

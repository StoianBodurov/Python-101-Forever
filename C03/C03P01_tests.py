from unittest import TestCase, main

from C03.C03P01 import Interval


class IntervalTests(TestCase):
    def test_is_inside_if_start_closed_end_closed_correct_result(self):
        interval = Interval(1, 10)

        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(10))

    def test_is_inside_if_start_closed_end_closed_incorrect_result(self):
        interval = Interval(1, 10)

        self.assertFalse(interval.is_inside(0))
        self.assertFalse(interval.is_inside(11))

    def test_is_inside_if_start_opened_end_closed_correct_result(self):
        interval = Interval(1, 10, start_opened=True)

        self.assertTrue(interval.is_inside(2))
        self.assertTrue(interval.is_inside(10))

    def test_is_inside_if_start_opened_end_closed_incorrect_result(self):
        interval = Interval(1, 10, start_opened=True)

        self.assertFalse(interval.is_inside(1))
        self.assertFalse(interval.is_inside(11))

    def test_is_inside_if_start_closed_end_opened_correct_result(self):
        interval = Interval(1, 10, end_opened=True)

        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(9))

    def test_is_inside_if_start_closed_end_opened_incorrect_result(self):
        interval = Interval(1, 10, end_opened=True)

        self.assertFalse(interval.is_inside(0))
        self.assertFalse(interval.is_inside(10))

    def test_is_inside_if_start_opened_end_opened_correct_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=True)

        self.assertTrue(interval.is_inside(2))
        self.assertTrue(interval.is_inside(9))

    def test_is_inside_if_start_opened_end_opened_incorrect_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=True)

        self.assertFalse(interval.is_inside(1))
        self.assertFalse(interval.is_inside(10))

    def test_stringify_start_closed_end_closed_produces_correct_result(self):
        interval = Interval(1, 10)
        expected = "[1, 10]"

        self.assertEqual(expected, interval.stringify())

    def test_stringify_start_opened_end_closed_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=True)
        expected = "(1, 10]"

        self.assertEqual(expected, interval.stringify())

    def test_stringify_start_closed_end_opened_produces_correct_result(self):
        interval = Interval(1, 10, end_opened=True)
        expected = "[1, 10)"

        self.assertEqual(expected, interval.stringify())

    def test_stringify_start_opened_end_opened_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=True)
        expected = "(1, 10)"

        self.assertEqual(expected, interval.stringify())


if __name__ == '__main__':
    main()
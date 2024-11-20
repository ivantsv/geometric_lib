import unittest


def area(a):
    '''Принимает число a - длину стороны квадрата, возвращает его площадь.'''
    return a * a


def perimeter(a):
    '''Принимает число a - длину стороны квадрата, возвращает его периметр.'''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        '''Тестирование площади с нулевой стороной.'''
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        '''Тестирование периметра с нулевой стороной.'''
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_result_area(self):
        '''Тестирование площади.'''
        res = area(10)
        self.assertEqual(res, 100)

    def test_result_perimeter(self):
        '''Тестирование периметра.'''
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_fractional_side_area(self):
        """Тестирование площади с дробной стороной."""
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_fractional_side_perimeter(self):
        """Тестирование периметра с дробной стороной."""
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10)

    def test_large_side_area(self):
        """Тестирование площади с большой стороной."""
        large_side = 1e6
        res = area(large_side)
        self.assertEqual(res, 1e6 ** 2)

    def test_large_side_perimeter(self):
        """Тестирование периметра с большой стороной."""
        large_side = 1e6
        res = perimeter(large_side)
        self.assertEqual(res, 4 * 1e6)

    def test_small_side_area(self):
        """Тестирование площади с очень малой стороной."""
        small_side = 1e-6
        res = area(small_side)
        self.assertAlmostEqual(res, small_side ** 2)

    def test_small_side_perimeter(self):
        """Тестирование периметра с очень малой стороной."""
        small_side = 1e-6
        res = perimeter(small_side)
        self.assertAlmostEqual(res, 4 * small_side)

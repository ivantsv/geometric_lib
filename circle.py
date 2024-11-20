import math
import unittest


def area(r):
    '''Принимает число r - радиус круга, возвращает его площадь.'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r - радиус окружности, возвращает ее длину.'''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        '''Тестирование площади с нулевым радиусом'''
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_radius_perimeter(self):
        '''Тестирование периметра с нулевым радиусом'''
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_result_area(self):
        '''Тестирование площади'''
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_result_perimeter(self):
        '''Тестирование периметра'''
        res = perimeter(10)
        self.assertEqual(res, math.pi * 20)

    def test_fractional_radius_area(self):
        """Тестирование площади с дробным радиусом."""
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 2.5 * 2.5)

    def test_fractional_radius_perimeter(self):
        """Тестирование периметра с дробным радиусом."""
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5)

    def test_large_radius_area(self):
        """Тестирование площади с большим радиусом."""
        large_radius = 1e6
        res = area(large_radius)
        self.assertEqual(res, math.pi * large_radius ** 2)

    def test_large_radius_perimeter(self):
        """Тестирование периметра с большим радиусом."""
        large_radius = 1e6
        res = perimeter(large_radius)
        self.assertEqual(res, 2 * math.pi * large_radius)

    def test_small_radius_area(self):
        """Тестирование площади с очень малым радиусом."""
        small_radius = 1e-6
        res = area(small_radius)
        self.assertAlmostEqual(res, math.pi * small_radius ** 2)

    def test_small_radius_perimeter(self):
        """Тестирование периметра с очень малым радиусом."""
        small_radius = 1e-6
        res = perimeter(small_radius)
        self.assertAlmostEqual(res, 2 * math.pi * small_radius)

import unittest


def area(a, h):
    '''Принимает число a - длину стороны треугольника и число h - длину высоты, опущенной на эту сторону.
    Возвращает площадь треугольника.'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает числа a, b, c - стороны треугольника. Возвращает его периметр.'''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_base_or_height_area(self):
        """Проверка площади треугольника с одной или обеими нулевыми величинами."""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_positive_base_and_height_area(self):
        """Проверка площади треугольника с положительными основаниями и высотами."""
        self.assertEqual(area(6, 4), 12)
        self.assertAlmostEqual(area(3.5, 2.8), 4.9)

    def test_zero_sides_perimeter(self):
        """Проверка периметра треугольника, если одна или несколько сторон равны нулю."""
        self.assertEqual(perimeter(0, 5, 7), 12)
        self.assertEqual(perimeter(5, 0, 7), 12)
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_positive_sides_perimeter(self):
        """Проверка периметра треугольника с положительными сторонами."""
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(perimeter(3.5, 2.8, 4.1), 10.4)

    def test_fractional_base_and_height_area(self):
        """Проверка площади треугольника с дробными основаниями и высотами."""
        self.assertAlmostEqual(area(0.5, 0.4), 0.1)
        self.assertAlmostEqual(area(2.5, 1.2), 1.5)

    def test_fractional_sides_perimeter(self):
        """Проверка периметра треугольника с дробными сторонами."""
        self.assertAlmostEqual(perimeter(1.5, 2.3, 3.2), 7.0)
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.3), 0.6)

    def test_large_base_and_height_area(self):
        """Проверка площади треугольника с большими основаниями и высотами."""
        self.assertEqual(area(1e6, 1e6), 5e11)

    def test_large_sides_perimeter(self):
        """Проверка периметра треугольника с большими сторонами."""
        self.assertEqual(perimeter(1e6, 1e6, 1e6), 3e6)

    def test_small_base_and_height_area(self):
        """Проверка площади треугольника с малыми основаниями и высотами."""
        self.assertAlmostEqual(area(1e-6, 1e-6), 5e-13)

    def test_small_sides_perimeter(self):
        """Проверка периметра треугольника с малыми сторонами."""
        self.assertAlmostEqual(perimeter(1e-6, 1e-6, 1e-6), 3e-6)

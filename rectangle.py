import unittest


def area(a, b):
    '''Принимает числа a и b - смежные стороны прямоугольника. Возвращает его площадь.'''
    return a * b

def perimeter(a, b):
    '''Принимает числа a и b - смежные стороны прямоугольника. Возвращает его периметр.'''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_sides_area(self):
        """Проверка площади прямоугольника с одной или обеими сторонами равными нулю."""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_zero_sides_perimeter(self):
        """Проверка периметра прямоугольника с одной или обеими сторонами равными нулю."""
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)

    def test_positive_sides_area(self):
        """Проверка площади прямоугольника с положительными сторонами."""
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(3, 7), 21)

    def test_positive_sides_perimeter(self):
        """Проверка периметра прямоугольника с положительными сторонами."""
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(3, 7), 20)

    def test_fractional_sides_area(self):
        """Проверка площади прямоугольника с дробными сторонами."""
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)
        self.assertAlmostEqual(area(0.1, 0.1), 0.01)

    def test_fractional_sides_perimeter(self):
        """Проверка периметра прямоугольника с дробными сторонами."""
        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)
        self.assertAlmostEqual(perimeter(0.1, 0.1), 0.4)

    def test_large_sides_area(self):
        """Проверка площади прямоугольника с большими сторонами."""
        self.assertEqual(area(1e6, 1e6), 1e12)

    def test_large_sides_perimeter(self):
        """Проверка периметра прямоугольника с большими сторонами."""
        self.assertEqual(perimeter(1e6, 1e6), 4e6)

    def test_small_sides_area(self):
        """Проверка площади прямоугольника с малыми сторонами."""
        self.assertAlmostEqual(area(1e-6, 1e-6), 1e-12)

    def test_small_sides_perimeter(self):
        """Проверка периметра прямоугольника с малыми сторонами."""
        self.assertAlmostEqual(perimeter(1e-6, 1e-6), 4e-6)

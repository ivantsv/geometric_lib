# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Project description
This project will help users to do common geometric operations (like calculating the perimeter and the area of some kind of figure).
Now it has formulas for 4 types of figures: rectangles, triangles, squares and circles.
1. rectangle.py
   - def area(a, b)
   - def perimeter(a, b)
2. triangle.py
   - def area(a, h)
   - def perimeter(a, b, c)
3. square.py
   - def area(a)
   - def perimeter(a)
4. circle.py
   - def area(r)
   - def perimeter(r)
You also need standart Python math library to get math.pi

# Functions
## Rectangle functions
1. area(a, b) -> return a * b [It gets rectangle sides. Than using common formula it searches its area.]
   - Ex.: area(5, 10) => 50
2. perimeter(a, b) -> return 2 * (a + b) [It gets rectangle sides. Than using common formula it searches its perimeter.]
   - Ex.: perimeter(5, 10) => 30
## Triangle functions
1. area(a, h) -> return a * h / 2 [It gets triangle side and height. Than using common formula it searches its area.]
   - Ex.: area(5, 10) => 25
2. perimeter(a, b, c) -> return a + b + c [It gets trinagle sides. Than using common formula it searches its perimeter.]
   - Ex.: perimeter(5, 10, 8) => 23
## Square functions
1. area(a) -> return a * a [It gets square side. Than using common formula it searches its area.]
   - Ex.: area(5) => 25
2. perimeter(a) -> return 4 * a [It gets square side. Than using common formula it searches its perimeter.]
   - Ex.: perimeter(5) => 20
## Circle functions
1. area(r) -> return math.pi * r * r [It gets circles radius. Than using common formula it searches its area.]
   - Ex.: area(5) => 78,5
2. perimeter(r) -> return 2 * math.pi * r [It gets circles radius. Than using common formula it searches its perimeter.]
   - Ex.: perimeter(5) => 31,4

# Story of changes
1. commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
   - Circle and square added
2. commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
   - Docs added
3. commit 33ff374df1ceeea181b93d788ae0941ae6f1cc25
   - Добавлен новый файл rectangle.py
4. commit 9efccab6f684bf1e0590a2545782720ecc3039e1
   - Исправлена ошибка в rectangle.py и добавлен файл triangle.py

# Testing
Added tests, to test any file write:
```cmd
python.exe -m unittest <file_name>.py
```
- Ex.: python.exe -m unittest rectangle.py

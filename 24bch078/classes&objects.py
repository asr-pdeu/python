# 12.1

class Complex:

    def _init_(self, real, imag):

        self.real = real

        self.imag = imag

 

    def add(self, other):

        return Complex(self.real + other.real, self.imag + other.imag)

 

    def subtract(self, other):

        return Complex(self.real - other.real, self.imag - other.imag)

 

    def multiply(self, other):

        r = self.real * other.real - self.imag * other.imag

        i = self.real * other.imag + self.imag * other.real

        return Complex(r, i)

 

    def divide(self, other):

        den = other.real*2 + other.imag*2

        r = (self.real * other.real + self.imag * other.imag) / den

        i = (self.imag * other.real - self.real * other.imag) / den

        return Complex(r, i)

 

    def display(self):

        print(f"{self.real} + {self.imag}i")

 

c1 = Complex(4, 3)

c2 = Complex(1, 2)

c1.add(c2).display()

c1.subtract(c2).display()

c1.multiply(c2).display()

c1.divide(c2).display()

 

 

 

# 12.2

class Matrix:

    def _init_(self, mat):

        self.mat = mat

 

    def add(self, other):

        result = [[self.mat[i][j] + other.mat[i][j] for j in range(3)] for i in range(3)]

        return Matrix(result)

 

    def multiply(self, other):

        result = [[0]*3 for _ in range(3)]

        for i in range(3):

            for j in range(3):

                for k in range(3):

                    result[i][j] += self.mat[i][k] * other.mat[k][j]

        return Matrix(result)

 

    def transpose(self):

        result = [[self.mat[j][i] for j in range(3)] for i in range(3)]

        return Matrix(result)

 

    def show(self):

        for row in self.mat:

            print(row)

 

m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])

m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

m1.add(m2).show()

m1.multiply(m2).show()

m1.transpose().show()

 

 

 

# 12.3

class Solid:

    def _init_(self, shape, values):

        self.shape = shape

        self.values = values

 

    def surface_area(self):

        if self.shape == "sphere":

            r = self.values

            return 4 * 3.14 * r * r

        elif self.shape == "cuboid":

            l, w, h = self.values

            return 2 * (l*w + w*h + h*l)

 

    def volume(self):

        if self.shape == "sphere":

            r = self.values

            return (4/3) * 3.14 * r**3

        elif self.shape == "cuboid":

            l, w, h = self.values

            return l * w * h

 

s = Solid("sphere", 3)

print("Surface Area:", s.surface_area())

print("Volume:", s.volume())

 

 

 

# 12.4

class Shape:

    def _init_(self, shape, size):

        self.shape = shape

        self.size = size

 

    def area(self):

        if self.shape == "circle":

            return 3.14 * self.size * self.size

        elif self.shape == "square":

            return self.size * self.size

 

    def perimeter(self):

        if self.shape == "circle":

            return 2 * 3.14 * self.size

        elif self.shape == "square":

            return 4 * self.size

 

s = Shape("circle", 5)

print("Area:", s.area())

print("Perimeter:", s.perimeter())

 

 

 

# 12.5

class Time:

    def _init_(self, h, m, s):

        self.h = h

        self.m = m

        self.s = s

 

    def add(self, other):

        s = self.s + other.s

        m = self.m + other.m + s // 60

        h = self.h + other.h + m // 60

        return Time(h % 24, m % 60, s % 60)

 

    def show(self):

        print(f"{self.h:02d}:{self.m:02d}:{self.s:02d}")

 

t1 = Time(2, 30, 45)

t2 = Time(1, 40, 30)

t1.add(t2).show()

 

 

 

# 12.6

class Date:

    def _init_(self, d, m, y):

        self.day = d

        self.month = m

        self.year = y

 

    def _eq_(self, other):

        return self.day == other.day and self.month == other.month and self.year == other.year

 

d1 = Date(22, 4, 2025)

d2 = Date(22, 4, 2025)

print("Dates are equal:", d1 == d2)

 

 

 

# 12.7

class Weather:

    def _init_(self, items):

        self.items = items

 

    def _contains_(self, item):

        return item in self.items

 

w = Weather(["Rain", "Cloudy", "Windy"])

print("Rain" in w)

print("Sunny" in w)

 

 

 

# 12.8

class MyString:

    def _init_(self, text):

        self.text = text

 

    def _iadd_(self, other):

        self.text += other.text

        return self

 

    def toLower(self):

        return self.text.lower()

 

    def toUpper(self):

        return self.text.upper()

 

s1 = MyString("Hello")

s2 = MyString("World")

s1 += s2

print("Joined:", s1.text)

print("Lower:", s1.toLower())

print("Upper:", s1.toUpper())

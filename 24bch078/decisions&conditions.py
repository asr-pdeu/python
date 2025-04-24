#2(a).1

a = 39

b = 31

x = (75 and a >= 20 and b < 60 and 35)

y = (-30 and a >= 20 and b < 15 and 35)

z = (-30 and a >= 20 and 0 and 35)

print("AND Results:")

print("x =", x) 

print("y =", y) 

print("z =", z) 

 

#2(a).2

a = 41

b = 29

x = 75 or a >= 20 and b < 60 and 35

x = 75 or a >= 20 or 60

y = a >= 20 or 75 or 60

z = a < 20 or 0 or 35

print("\nOR Results:")

print("x =", x) 

print("y =", y) 

print("z =", z) 

 

#2(a).3

a = 9

b = 34

result = not (a <= b)

print("\nNOT Result:")

print("result =", result)

 

 

 

 

#2(b).1

x = int(input("Enter the 1st number: "))

y = int(input("Enter the 2nd number: "))

if x > y:

    print("Largest Number:", x)

    print("Smallest Number:", y)

else:

    print("Largest Number:", y)

    print("Smallest Number:", x)

 

#2(b).2

x = int(input("Enter the 1st number: "))

y = int(input("Enter the 2nd number: "))

z = int(input("Enter the 3rd number: "))

if x > y and x > z:

    print("Largest Number:", x)

elif y > z:

    print("Largest Number:", y)

else:

    print("Largest Number:", z)

if x < y and x < z:

    print("Smallest Number:", x)

elif y < z:

    print("Smallest Number:", y)

else:

    print("Smallest Number:", z)

 

#2(b).3

n = int(input("Enter a number: "))

if n % 2 == 0:

    print("The Number is Even")

else:

    print("The Number is Odd")

 

#2(b).4

n = int(input("Enter a number: "))

if n % 10 == 0:

    print("The Number is Divisible by 10")

else:

    print("The Number is Not Divisible by 10")

 

#2(b).5

age = int(input("Enter Age: "))

if age < 18:

    print("The Person is Minor")

else:

    print("The Person is Not Minor")

 

#2(b).6

n = int(input("Enter a number: "))

n = abs(n)

count = 0

if n == 0:

    count = 1

else:

    while n > 0:

        count += 1

        n //= 10

print("Number of digits:", count)

 

#2(b).7

year = int(input("Enter a Year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

    print("It is a Leap Year")

else:

    print("It is Not a Leap Year")

 

#2(b).8

a = int(input("Enter Angle x: "))

b = int(input("Enter angle y: "))

c = int(input("Enter angle z: "))

if a + b + c == 180:

    print("The Triangle is Valid ")

else:

    print("The Triangle is Invalid ")

 

#2(b).9

n = int(input("Enter a Number: "))

if n < 0:

    print("The Absolute Value is:", -n)

else:

    print("The Absolute Value is:", n)

 

#2(b).10

length = int(input("Enter the Length: "))

breadth = int(input("Enter the Breadth: "))

area = length * breadth

perimeter = 2 * (length + breadth)

if area > perimeter:

    print("Area is Greater than the Perimeter")

else:

    print("Perimeter is Greater than the Area")

 

#2(b).11

x1 = int(input("x1: "))

y1 = int(input("y1: "))

x2 = int(input("x2: "))

y2 = int(input("y2: "))

x3 = int(input("x3: "))

y3 = int(input("y3: "))

if (y2 - y1)(x3 - x1) == (y3 - y1)(x2 - x1):

    print("The Points are Collinear")

else:

    print("The Points are not Collinear")

 

#2(b).12

x = int(input("Enter x: "))

y = int(input("Enter y: "))

cx = int(input("Enter Center x: "))

cy = int(input("Enter Center y: "))

r = int(input("Enter the Radius: "))

d = math.sqrt((x - cx)*2 + (y - cy)*2)

if d < r:

    print("The Point is Inside the Circle")

elif d == r:

    print("The Point is On the Circle")

else:

    print("The Point is Outside the Circle")

 

#2(b).13

n = int(input("Enter a Number Between (0-19): "))

words = ["zero", "one", "two", "three", "four", "five", "six", "seven",

         "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",

         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

if 0 <= n <= 19:

    print(words[n])

else:

    print("Out of range")

 

#2(b).14

marks1 = int(input("Enter marks of subject 1: "))

marks2 = int(input("Enter marks of subject 2: "))

marks3 = int(input("Enter marks of subject 3: "))

total marks = marks1 + marks2 + marks3

avg = total marks / 3

print("Total Marks:", total marks)

print("Average Marks:", avg)

if m1 <= 39 or m2 <= 39 or m3 <= 39:

    print("Result:  Fail")

else:

    print("Result:  Pass")

for marks in [marks1, marks2, marks3]:

    if marks == 0:

        print("Grade:  NA")

    elif marks <= 39:

        print("Grade:  F")

    elif marks <= 44:

        print("Grade:  P")

    elif marks <= 49:

        print("Grade:  C")

    elif marks <= 54:

        print("Grade:  B")

    elif marks <= 59:

        print("Grade:  B+")

    elif marks <= 69:

        print("Grade:  A")

    elif marks <= 79:

        print("Grade:  A+")

    elif marks <= 100:

        print("Grade:  O")

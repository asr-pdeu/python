# 9(a).1

def fun():

    print("This is fun()")

 

def disp():

    print("This is disp()")

 

def msg():

    print("This is msg()")

 

functions = [fun, disp, msg]

for f in functions:

    f()

 

 

 

# 9(a).2

list1 = [6, 7, 8, 9, 5, 1]

list2 = [1, 5, 9, 8, 7, 6]

result = list(map(lambda x, y: x + y, list1, list2))

print("Resultant list:", result)

 

 

 

# 9(a).3

import random

numbers = random.sample(range(-15, 16), 10)

squares = list(map(lambda x: x**2, numbers))

print("Random numbers:", numbers)

print("Squares:", squares)

 

 

 

# 9(a).4

lst = ['madam', 'Python', "malayalam", 12321]

palindromes = list(filter(lambda x: isinstance(x, str) and x == x[::-1], lst))

print("Palindrome strings:", palindromes)

 

 

 

# 9(a).5

faculty_names = ['Alexander', 'Bob', 'Catherine', 'John', 'Elizabeth', 'Mike', 'Christina']

long_names = list(filter(lambda name: len(name) > 8, faculty_names))

print("Names longer than 8 characters:", long_names)

 

 

 

 

#9(b.1).1

def count_lower_upper(s):

    result = {'lowercase': 0, 'uppercase': 0}

    for char in s:

        if char.islower():

            result['lowercase'] += 1

        elif char.isupper():

            result['uppercase'] += 1

    return result

 

print(count_lower_upper("Hello World! Functional Programming Rocks."))

 

 

 

#9(b.1).2

def compute(n):

    n = str(n)

    return int(n) + int(n*2) + int(n*3) + int(n*4)

 

for i in range(4, 8):

    print(f"compute({i}) =", compute(i))

 

 

 

#9(b.1).3

def create_array(x, y, z, val):

    return [[[val for _ in range(z)] for _ in range(y)] for _ in range(x)]

 

array = create_array(3, 4, 5, 7)

print("3D array created with value 7 at all positions.")

 

 

 

#9(b.1).4

def sum_avg(marks):

    total = sum(marks)

    avg = total / len(marks)

    return total, avg

 

print("Sum and Avg:", sum_avg([80, 90, 85, 95, 100]))

 

 

 

#9(b.1).5

def ispangram(sentence):

    return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence.lower())

 

print(ispangram("The quick brown fox jumps over the lazy dog"))

print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))

 

 

 

#9(b.1).6

def power_tuples(n):

    return [(x, x*2, x*3) for x in range(1, n+1)]

 

print("Tuples:", power_tuples(5))

 

 

 

#9(b.1).7

def ispalindrome(s):

    s_cleaned = ''.join(filter(str.isalnum, s)).lower()

    return s_cleaned == s_cleaned[::-1]

 

print(ispalindrome("A man a plan a canal Panama"))

print(ispalindrome("Hello"))

 

 

 

#9(b.1).8

def convert(s):

    words = s.split()

    unique_sorted = sorted(set(words))

    return ' '.join(unique_sorted)

 

print(convert("hello world hello python world code"))

 

 

 

#9(b.1).9

def count_alpha_digits(s):

    result = {'alphabets': 0, 'digits': 0}

    for char in s:

        if char.isalpha():

            result['alphabets'] += 1

        elif char.isdigit():

            result['digits'] += 1

    return result

 

print(count_alpha_digits("abc123ABC456xyz"))

 

 

 

#9(b.1).10

def frequency(text):

    words = text.split()

    freq = {}

    for word in words:

        freq[word] = freq.get(word, 0) + 1

    return dict(sorted(freq.items()))

 

print(frequency("apple banana apple orange banana apple"))

 

 

 

#9(b.1).11

def create_list(list1, list2):

    return list(set(list1) & set(list2))

 

print(create_list([1, 2, 3]))

 

 

 

 

#9(b.2).1

def prime_factors(n, i=2):

    if n < 2:

        return []

    if n % i == 0:

        return [i] + prime_factors(n // i, i)

    return prime_factors(n, i + 1)

 

print("Prime factors of 84:", prime_factors(84))

 

 

 

#9(b.2).2

def to_binary(n):

    if n == 0:

        return '0'

    if n == 1:

        return '1'

    return to_binary(n // 2) + str(n % 2)

 

print("Binary of 18:", to_binary(18))

 

 

 

#9(b.2).3

def count_vowels(s):

    if not s:

        return 0

    return (1 if s[0].lower() in 'aeiou' else 0) + count_vowels(s[1:])

 

print("Vowel count:", count_vowels("Functional Programming Rocks"))

 

 

 

#9(b.2).4

def reverse_list(lst):

    if len(lst) <= 1:

        return lst

    return [lst[-1]] + reverse_list(lst[:-1])

 

print("Reversed list:", reverse_list([1, 2, 3, 4, 5]))

 

 

 

#9(b.2).5

def power(a, b):

    if b == 0:

        return 1

    return a * power(a, b - 1)

 

print("3^4 =", power(3, 4))

 

 

 

#9(b.2).6

def sanitize_list(lst):

    if not lst:

        return []

    head = 0 if lst[0] < 0 else lst[0]

    return [head] + sanitize_list(lst[1:])

 

print("Sanitized list:", sanitize_list([-1, 5, -3, 7, 0, -2]))

 

 

 

#9(b.2).7

def average_list(lst):

    def helper(lst, total=0, count=0):

        if not lst:

            return total / count if count > 0 else 0

        return helper(lst[1:], total + lst[0], count + 1)

    return helper(lst)

 

print("Average:", average_list([10, 20, 30, 40, 50]))

 

#9(b.2).8

def string_length(s):

    if s == '':

        return 0

    return 1 + string_length(s[1:])

 

print("Length of the string:", string_length("Recursion"))      

 

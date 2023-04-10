def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else: return "Odd"

print(even_or_odd(5))
print(even_or_odd(6))
print(even_or_odd(-36))
#write a function that greets the owner with hello boss, and a guest with hello guest
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else: return "Hello guest"
print(greet("tom","tom"))
print(greet("tom","Brandon"))
print(greet("tim","tim"))

# Write a function `greet` that returns "hello world!"
def greet():
    return "hello world!"
print(greet())

#make positive numbers negative, negative numbers stay the same, zero is zero
def make_negative( number ):
    
    if number > 0:
        number = str(number)
        number = "-" + number
        number = int(number)
        return number
    elif number < 0:
        return number
    elif number == 0:
        return 0
print(make_negative(4))
print(make_negative(-3))
print(make_negative(-12))
print(make_negative(1))

def find_average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)
print(find_average([1, 2, 3]))

def bmi(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"
print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(110, 1.80))

# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
def grow(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult


def opposite(number):
    if number < 0:
        number = str(number)
        number = number.split('-')
        number = number[1]
        number = eval(number)
        return number
    if number > 0:
        number = str(number)
        number = "-" + number
        number = eval(number)
        number = float(number)
        return number
    elif number == 0:
        return 0
    

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output

def basic_op(operator, value1, value2):
    if operator == '+':
        sum = value1 + value2
        return sum 

    if operator == '-':
        sum = value1 - value2
        return sum 

    if operator == '*':
        sum = value1 * value2
        return sum

    if operator == '/':
        sum = value1 / value2
        return sum 
    
def quarter_of(month):
        if 1<= month <= 3:
            return 1
        elif  month <= 6 and month > 3:
            return 2
        elif month <= 9 and month > 6:
            return 3
        elif  month <= 12 and month >= 9:
            return 4
print(quarter_of(8))


def better_than_average(class_points, your_points):
    class_sum = sum(class_points)
    class_avg = class_sum/len(class_points)
    if your_points > class_avg:
        return True
    else:
        return False
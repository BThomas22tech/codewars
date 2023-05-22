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

# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return f"Hello, {name} how are you doing today?"
print(greet("John"))


def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i
    return sum 

def count_by(x, n):
    num = []
    for i in range(1,n+1):
        results = x * i
        num.append(results)
    return num


def xo(s):
    x_count = 0
    o_count = 0
    for i in range(len(s)):
        if s[i] == "x" or s[i] == "X":
            x_count += 1
        elif s[i] == "o" or s[i]=="O":
            o_count += 1
    if x_count == o_count:
            return True
    else: return False

def friend(x):
    friend = []
    for i in x:
        if len(i) == 4:
            friend.append(i)
    return friend
#sum a two digit number ex. 11 = 2
def solution(n):
    n = str(n)
    number = int(n[0]) + int(n[1])
    return number
print(solution(11))
print(solution(33))
print(solution(14))
def solution(input):
    num = str(input)
    for num in input:
        if num == num :
            return True
        
print(solution([1,1]))

def get_sum(a,b):
    #use sum variable
    sum = 0
    if a == b:
        return a
    #looop with range
    elif a > b:
        for i in range(b,a+1):
            sum += i
        return sum
    else:
        for i in range(a,b+1):
            sum += i
        return sum
    

def sum_two_smallest_numbers(numbers):
    #use sort function
    numbers.sort()
    #get number by index
    num1 = numbers[0]
    num2 = numbers[1]
    #add numbers to sum
    sum = num1 + num2
    #return sum
    return sum

#     You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

# Write a program that returns the girl's age (0-9) as an integer.

# Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.
def get_age(age):
    number = int(age[0])
    print(number)
    return number

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA != headB:
            if headA == None:
                headA = headB
            else: 
                headA = headA.next
            if headB == None:
                headB = headA
            else: 
                headB = headB.next

        # return headA
    
        a=headA
        b=headB
        while a!=b:
            if a==None:
                a=headB
            else:
                a=a.next
            if b==None:
                b=headA
            else:
                b=b.next
        return a


def unique(string):
    dict = {"a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0,
            "f":0,
            "g":0,
            "h":0, 
            "i":0, 
            "j":0,
            "k":0,
            "l":0,
            "m":0,
            "n":0,
            "o":0,
            "p":0,
            "q": 0,
            "r":0,
            "s":0,
            "t":0,
            "u":0,
            "v":0,
            "w":0,
            "x":0,
            "y":0,
            "z":0}
    for i in string:
        if i in dict:
            dict[i] += 1
    for k in dict:
        if dict[k] <= 1:
            print(k, "is unique")
        else: print(k, "is not unique")
    return dict

# print(unique("high"))
# print(unique("cool"))
# print(unique("egg"))

# given two strings write a method to decide if one is a permutation of the other.
def permutation(string1,string2):
    if len(string1) != len(string2):
        return False
    list_one = list(string1)
    list_one.sort()
    list_two = list(string2)
    list_two.sort()
    if list_one == list_two:
        return True
    else: return False
    # return [list_one,list_two]
print(permutation("dog","dgo"))
print(permutation("car","dog"))

# write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

def URLify(string):
    list = []
    for i in string:
        if i == " ":
            list.append("%20")
        else:
            list.append(i)
    modified_string = ''.join(list)
    return modified_string


print(URLify("Mr John Smith  "))
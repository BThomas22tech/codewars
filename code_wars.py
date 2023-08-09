def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(5))
print(even_or_odd(6))
print(even_or_odd(-36))
# write a function that greets the owner with hello boss, and a guest with hello guest


def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


print(greet("tom", "tom"))
print(greet("tom", "Brandon"))
print(greet("tim", "tim"))

# Write a function `greet` that returns "hello world!"


def greet():
    return "hello world!"


print(greet())

# make positive numbers negative, negative numbers stay the same, zero is zero


def make_negative(number):

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
    if 1 <= month <= 3:
        return 1
    elif month <= 6 and month > 3:
        return 2
    elif month <= 9 and month > 6:
        return 3
    elif month <= 12 and month >= 9:
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
    for i in range(1, n+1):
        results = x * i
        num.append(results)
    return num


def xo(s):
    x_count = 0
    o_count = 0
    for i in range(len(s)):
        if s[i] == "x" or s[i] == "X":
            x_count += 1
        elif s[i] == "o" or s[i] == "O":
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False


def friend(x):
    friend = []
    for i in x:
        if len(i) == 4:
            friend.append(i)
    return friend
# sum a two digit number ex. 11 = 2


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
        if num == num:
            return True


print(solution([1, 1]))


def get_sum(a, b):
    # use sum variable
    sum = 0
    if a == b:
        return a
    # looop with range
    elif a > b:
        for i in range(b, a+1):
            sum += i
        return sum
    else:
        for i in range(a, b+1):
            sum += i
        return sum


def sum_two_smallest_numbers(numbers):
    # use sort function
    numbers.sort()
    # get number by index
    num1 = numbers[0]
    num2 = numbers[1]
    # add numbers to sum
    sum = num1 + num2
    # return sum
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

        a = headA
        b = headB
        while a != b:
            if a == None:
                a = headB
            else:
                a = a.next
            if b == None:
                b = headA
            else:
                b = b.next
        return a


def unique(string):
    dict = {"a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0}
    for i in string:
        if i in dict:
            dict[i] += 1
    for k in dict:
        if dict[k] <= 1:
            print(k, "is unique")
        else:
            print(k, "is not unique")
    return dict

# print(unique("high"))
# print(unique("cool"))
# print(unique("egg"))

# given two strings write a method to decide if one is a permutation of the other.


def permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    list_one = list(string1)
    list_one.sort()
    list_two = list(string2)
    list_two.sort()
    if list_one == list_two:
        return True
    else:
        return False

    # return [list_one,list_two]
print(permutation("dog", "dgo"))
print(permutation("car", "dog"))

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


def is_pal_perm(input_string):
    input_string = input_string.replace(" ", "")
    input_string = input_string.lower()
    d = dict()
    for i in input_string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    odd_count = 0
    for key, value in d.items():
        if value % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif value % 2 != 0 and odd_count != 0:
            return False
    return True


print(is_pal_perm("tact Coa"))
print(is_pal_perm("racecar"))
print(is_pal_perm("raceca"))


def add_binary(a, b):
    sum = a + b
    binary = bin(sum)[2:]
    return binary


print(add_binary(1, 1))
print(add_binary(1, 3))
print(add_binary(5, 1))


def correct(s):
    new_string = ''
    for i in s:
        if i == "0":
            new_string += "O"
        elif i == "5":
            new_string += "S"
        elif i == "1":
            new_string += "I"
        else:
            new_string += i
    return new_string


print(correct("L0ND0N"))
print(correct("L0ND0N"))
print(correct("DUBL1N"))
print(correct("51NGAP0RE"))


def stray(arr):
    count_dict = {}
    new_array = []
    for i in arr:
        new_array.append(i)
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num


def century(year):
    if year % 100 == 0:
        return year//100
    else:
        return year//100+1


print(century(1705))


def get_volume_of_cuboid(length, width, height):
    V = length * width * height

    return V


def string_to_array(s):
    word = s.split()
    empty = s.split(" ")

    return empty


def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"


def smash(words):
    s = " ".join(words)
    return s
# takes individual words from an array and puts them into a sentence


def check_for_factor(base, factor):
    if base % factor != 0:
        return False
    if base % factor == 0:
        return True


def area_or_perimeter(l, w):
    if l == w:
        A = l * w
        return A
    if l != w:
        P = (l + w) * 2
        return P


def string_to_number(s):
    s = int(s)
    return s


def string_compression(string):
    compressed_string = ""
    current_letter = string[0]
    count = 1

    for i in range(1, len(string)):
        if string[i] == current_letter:
            count += 1
        else:
            compressed_string += current_letter + str(count)
            current_letter = string[i]
            count = 1
    # Add the count of the last letter
    compressed_string += current_letter + str(count)

    return compressed_string


print(string_compression("bcd"))
print(string_compression("aabcccaaa"))


def binary_search(input_array, value):
    right = len(input_array) - 1
    left = 0

    while left <= right:
        mid = (left + right) // 2

        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    else:
        output = get_fib(position - 1) + get_fib(position - 2)
        return output


def quicksort(array):
    if len(array) < 1:
        return array
    pivot = array[0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North_America': {'USA': ['Mountain View', 'Atlanta']},
             "Asia": {'India': ['Bangalore'], 'China': ['Shanghai']
                      }}
asia1city = locations['Asia']['India']
asia2city = locations['Asia']['China']
asiacountry = locations['Asia']
usa = locations['North_America']['USA']
usa.sort()
USA_City = ''
# for key,value in locations.items():
#     if key == 'USA':
#       # print(key,value)
print("1")
for city in usa:
    USA_City += city + "\n"
print(USA_City)

print("2")
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append((city, country))
asia_cities.sort()
for city, country in asia_cities:
    print(city + "-" + country)
"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            self.table[hash_value].append(string)
        else:
            self.table[hash_value] = [string]
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None and string in self.table[hash_value]:
            return hash_value
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')


def sockMerchant(n, ar):
    count = 0
    color_count = {}

    # Count the number of occurrences of each color
    for color in ar:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # Count the number of pairs for each color
    for color_count_value in color_count.values():
        count += color_count_value // 2

    return count


def reverse_vowel(string):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    new_string = ""
    vowel_indices = []
    for i in string:
        if i in vowels_list:
            vowel_indices.append(i)

    for i in string:
        if i in vowels_list:
            new_string += vowel_indices.pop()
        else:
            new_string += i
    return new_string


print(reverse_vowel("hello"))
print(reverse_vowel("python"))

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    count = 0
    count2 = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        if a[i] > b[i]:
            count += 1
        if a[i] < b[i]:
            count2 += 1
    return count, count2

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    dict = {}
    for candle in candles:
        if candle in dict:
            dict[candle] += 1
        else:
            dict[candle] = 1
    for key, value in dict.items():
        if value > 1:
            return value



def timeConversion(s):
    zone = s[-2:]
    time = s[:2]
    print(time)
    minutes = s[2:-2]
    hour = 0
    
    if zone == "PM" and int(time) ==12:
        new_time = str(time) +str(minutes)
        return new_time
    if zone == "PM":
        hour += int(time) + 12
        new_time = str(hour) + str(minutes)
        print(new_time)
        return new_time
    
    if zone == "AM" and int(time) == 12:
        new_time = '00' +str(minutes)
        return new_time
        
    else:
        return str(time) + str(minutes)
    
def breakingRecords(scores):
    first_score = scores[0]
    highest_score = first_score
    lowest_score = first_score
    h_score_count = 0
    l_score_count = 0
    
    for score in scores:
        if score >highest_score and score != highest_score:
            highest_score = score
            h_score_count += 1
        elif score < lowest_score and score != lowest_score:
            lowest_score = score
            l_score_count += 1
   
    
    return h_score_count,l_score_count
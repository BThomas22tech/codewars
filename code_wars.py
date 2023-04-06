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
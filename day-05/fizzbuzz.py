#Fizz Buzz
# Fizz - divisble by 3 
# Buzz - divisible by 5
# FizzBuzz - divisible both 3 and 5

for n in range(1, 11):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
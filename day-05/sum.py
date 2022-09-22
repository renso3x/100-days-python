# Sum of all even numbers in 1 - 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(f"The sum of all even numbers in 1 - 100 is {total}")
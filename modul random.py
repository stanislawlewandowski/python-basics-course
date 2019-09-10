import random

number1 = random.randint(1, 1000)
counter = 1
number2 = random.randint(1, 1000)

while number1 != number2:
    counter += 1
    number2 = random.randint(1, 1000)

print('number 1 is:', number1)
print('number 2 is:', number2)
print('number of attempts:', counter)



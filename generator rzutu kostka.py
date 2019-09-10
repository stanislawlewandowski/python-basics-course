import random
dice_range = range(1, 6)
dice = random.choice(dice_range)
if dice == 1:
    print('o')
elif dice == 2:
    print('\to \no')
elif dice == 3:
    print('\t\to\n\to\no')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')

dices = []
for i in range(5):
    dices.append(random.choice(dice_range))
random.shuffle(dices)
print(dices)


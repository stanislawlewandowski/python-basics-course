numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
max = len(numbers) - 2

while i < max:
    print(i, numbers[i], numbers[i+1], numbers[i+2])
    i += 1

    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print('found:', numbers[i], numbers[i+1], numbers[i+2])

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

z = 0
lastL = len(texts) - 1

while z < lastL:
    print(texts[z], texts[z+1])
    z += 1

    if len(texts[z + 1]) == len(texts[z]):
        print('\tFOUND')

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for s in range(10):
    print(string_A)

for z in range (9):
    print(string_A, '\n', string_B)


for i in range(1,10):
    print('x'*i)

for p in range(1,10):
    if p % 2 == 0:
        print("x"*p)
    else:
        print("o"*p)
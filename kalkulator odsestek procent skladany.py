initialCapital = 20000
percent = 0.03
percent2 = 1.03
maxTimeYears = 100
year = 0


while year < maxTimeYears:
    year += 1
    currentCapital = float(initialCapital*percent2**year)
    print(year, round(currentCapital, 2))


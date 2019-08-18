for candidate in range (2, 31):
    for divider in range (2,candidate):
        if candidate % divider == 0:
            print(candidate, 'to nie jest liczba pierwsza, dzieli sie przez', divider)
            break
        else:
            print(candidate, 'to liczba pierwsza')
            break


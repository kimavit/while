word = input()
counter = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    counter += 1
    word = input()
print(counter)

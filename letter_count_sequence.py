sequence = str(input("input sequence: "))
count = 0
for i in sequence:
    if i == 'A':
        count = count + 1

print('A occurs ', count, 'times')

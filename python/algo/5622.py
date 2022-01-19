call = input()

total = 0
for i in call:
    if i == 'A' or i == 'B' or i == 'C':
        total += 2
        total += 1
    if i == 'D' or i == 'E' or i == 'F':
        total += 3
        total += 1
    if i == 'G' or i == 'H' or i == 'I':
        total += 4
        total += 1
    if i == 'J' or i == 'K' or i == 'L':
        total += 5
        total += 1
    if i == 'M' or i == 'N' or i == 'O':
        total += 6
        total += 1
    if i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        total += 7
        total += 1
    if i == 'T' or i == 'U' or i == 'V':
        total += 8
        total += 1
    if i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        total += 9
        total += 1
print(total)
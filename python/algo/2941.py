S = input()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    if i in S:
        S = S.replace(i, '1')
print(len(S))
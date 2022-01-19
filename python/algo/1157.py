DD = input()
# print(ord('A')) 65
# print(ord('a')) 97

arr = {}
for i in range(26):
    arr[chr(65+i)] = 0
for i in DD:
    # 소문자
    temp = i
    if ord(i) > 96:
        temp = i.upper()
    arr[temp] += 1
print(arr)
max = -1
max_idx = -1
for idx, value in arr.items():
    if value > max:
        max = value
        max_idx = idx
    elif value == max:
        max_idx = '?'
print(max_idx)

# for idx, value in arr.items():
#     if idx == max_idx:
#         if idx == 'Z':
#             print(max_idx)
#             break
#         else: 
#             continue
#     if value == max:
#         print('?')
#         break
#     if idx == 'Z':
#         print(max_idx)

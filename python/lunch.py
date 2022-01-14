# import시 주의할 점
# import : 가지고 오는 행위
# 이 이후로 활용할 코드를 가지고 올 것이기 때문에 
# import는 항상 최 상단에 작성한다.
from calendar import c
import random

menu = ['짜장면', '짬뽕', '탕수육']

choice = random.choice(menu)

print(menu)
print(choice)

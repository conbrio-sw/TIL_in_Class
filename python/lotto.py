

# 1~45 중에 6개만 뽑아서 리스트에 담아서 출력
import random
from tkinter import N

# requests 불러오기
import requests
# requests 사용해서 로또 api에 데이터 요청
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997"
response = requests.get(url).json()
# 요청 보내서 응답 받은 문서를 출력
#print(response)
# 당첨 번호 정보를 리스트에 담아보자
winners = []
for i in range(1, 7):
    # print(response[f'drwtNo{i}'])
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{i}'])

print(winners)

numbers = list(range(1,46))
print(numbers)
# lotto = list(random.sample(numbers, 6))
# print(lotto)


for i in range(100):
    lotto = list(random.sample(numbers, 6))
    # 당첨 횟수를 기록
    count = 0
    for num in lotto:
        if num in winners:
            count += 1        
     # 6개 당첨 == 1등
    if count == 6:
         print(f"{i}번째에 당첨")
         break

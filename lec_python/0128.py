# 웹 사이트의 정보를 가지고 오고 싶다.
import requests
from bs4 import BeautifulSoup
from pprint import pprint


# 1-1. 주소
URL = 'https://finance.naver.com/sise/'
# 1-2. 요청
response = requests.get(URL)
#print(response, type(response))
# print(response.text)
# print(type(response.text)) # type : str

# 2-1 BeautifulSoup (text -> 다른 객체)
#KOSPI_now
data = BeautifulSoup(response.text, 'html.parser')
# print(data)
# print(type(data)) # type : <class 'bs4.BeautifulSoup'>

# 2-2 내가 원하는 정보를 찾는다
# 선택자를 활용한다.
kospi = data.select_one('#KOSPI_now')
print(kospi.text)


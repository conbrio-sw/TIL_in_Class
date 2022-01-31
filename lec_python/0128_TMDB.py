
import requests
from pprint import pprint       
# 1. URL 및 요청 변수 설정
BASE_URL = 'https://api.themoviedb.org/3'
api_key = '852609f6a97b603c24b48ba41963fca2'
path = '/movie/now_playing'
params = {
    'api_key' : api_key,
    'region' : 'KR',
    'language' : 'ko'
}


# 2. 요청 보낸 결과 저장
response = requests.get(BASE_URL+path, params)
print(response.status_code, response.url)
data = response.json()
# 3. 조작
# pprint(response)
pprint(len(data.get('results')))
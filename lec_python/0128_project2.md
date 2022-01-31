# 파이썬을 활용한 데이터 수집 2

### 목표

- 파이썬 기초 문법 실습
- 데이터 구조에 대한 분석과 이해
- 요청과 응답에 대한 이해
- API의 활용과 문서 분석

### 프로젝트 안내

- 외부 데이터를 수집하여 원하는 결과를 도출하기
  - 인기 영화 조회
  - 특정 조건에 맞는 인기 영화 조회
  - 특정 조건에 맞는 인기 영화 조회
  - 특정 영화 추천 영화 조회
  - 특정 영화 배우, 감독 리스트 조회

### 웹 스크래핑 (웹 크롤링)

- 요청과 응답
  - 요청 -> 주소(url) -> 응답
  - 요청 <- 문서(HTML, XML, JSON 등) <- 응답

- requests
  - simple HTTP library for Python
- BeautifulSoup
  - HTML, XML에 있는 데이터를 뽑아주는 친구

- 순서

  - 주소를 가져온다

    ```python
    URL = 'https://finance.naver.com/sise/'
    ```

  - 요청

    ```python
    response = requests.get(URL)
    # 프린트 시
    # print(response, type(response))
    >>> <Response [200]> <class 'requests.models.Response'>
    ```

    - `<Response [200]>` : 제대로 요청에 응했다. 성공적으로 가져왔다.

  - 파싱 및 활용

    - 텍스트 데이터를 HTML 구조로 변환하고
    - 원하는 정보를 뽑아서 출력한다.

    ```python
    from bs4 import BeautifulSoup
    
    data = BeautifulSoup(response.text, 'html.parser')
    kospi = data.select_one('#KOSPI_now')
    print(kospi.text)
    ```

### API(Application Programming Interface)

- 컴퓨터나 컴퓨터 프로그램 사이의 연결
- 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공
- 사용하는 방법을 기술하는 문서나 표준은 API 사양/명서 (sepification)

- API 명세서에서 어떤 정보를 확인해야할까?
  - 주소
  - 문서의 형태
- API 활용하는 법
  - 요청하는 방식에 대한 이해
    - 인증 방식
    - URL 생성
      - 기본 주소
      - 원하는 기능에 대한 추가 경로
      - 요청 변수(필수와 선택)
  - 응답 결과에 대한 이해
    - 응답 결과 타입(JSON)
    - 응답 결과 구조

### TMDB 활용

```python

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
response = requests.get(BASE_URL+path, params = params)
# url로 만들어주는 작업...
print(response.status_code, response.url)
data = response.json()
# 3. 조작
# pprint(response)
pprint(len(data.get('results')))
```


















































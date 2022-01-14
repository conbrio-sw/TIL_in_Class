- 코드가 쉬워졌다.
- 환경이 좋아졌다.
  - 오픈 소스 : 제작자의 권리를 지키면서, 누구나 코드 열람이 가능한, 오픈 소스 라이센스가 등장.
  - 공동 참여 프로젝트가 많아짐
  - 기술 이해만 있다면 누구든 활용 가능



# 파이썬의 기초

- 인생은 짧고 너는 파이썬이 필요하다.
- 프로그래밍 언어 == 컴퓨터에게 무언가를 시킬 때 쓰는 말
- 쉽고 많은 사람들이 사용, 많은 것을 활용

### 시작하기 전에...

- 대/소문자
- 띄어쓰기
- 스펠링

	# 파이썬의 문법

- 저장

  - 박스에 이름을 쓰고 그 안에 값을 넣는다.
  - dust = 60 // dust에 60을 저장(할당)한다.
  - 무엇을 저장하는가?
    - 숫자
    - 글자 : 따옴표로 둘러싼 글자 or 숫자
    - 참/거짓
  - 어떻게 저장하는가
    - 변수
      - 저장된 값을 변경할 수 있는 (variable) 박스
    - 리스트
      - 박스의 리스트, 박스가 순서대로 여러 개가 붙어 있다.
    - 딕셔너리
      - 궁극의 박스 dictionary
      - 견출지 붙인 박스들의 묶음
      - dust = {'영등포구' : 58, '강남구': 40}

- 조건

  - f'{dust} 따옴표'
  - "{0}따옴표.format(dust)"

- 반복

  - while

  - for

  - ```python
    for i in range(0, 4):
        print(greeting)
    while n < 4:
        print(greeting)
        n += 1
    ```

- Random
  - random.choice(list)
    - list안에 있는 무작위 값을 반환한다.
  - random.sample(리스트, 개수)
    - 리스트에서 특정 수의 요소를 임의적으로 비복원추출
    - ex) random.sample(numbers, 6) : 리스트로 반환하는 듯...

# API

- 요청(정보를 원하는 사람) -----주소(Url)------>
- <----문서(HTML/JSON)-------응답(정보를 주는 사람)
- 날씨 API : (https://www.metaweather.com/api/)

### JSON (JavaScrpit Object Notation)

- 데이터만을 주고 받기 위한 표기법

```python
# requests 불러오기
import requests
# requests 사용해서 로또 api에 데이터 요청
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997"
response = requests.get(url).json()
# 요청 보내서 응답 받은 문서를 출력
print(response)   #json 없으면 200반환 200: 요청이 잘 처리되었다는 뜻
for i in range(1, 7):
    print(response[f'drwtNo{i}']) # 로또번호 6개 출력
```
























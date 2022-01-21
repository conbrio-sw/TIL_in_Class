# PJT 01. Python을 활용한 데이터 수집 l

### TIL

- 이번 실습을 하면서 배운 것 중 가장 큰 것은 .JSON 파일을 사용하는 법이다.
  - 정확하게 배운 것은 아니지만 코드 예제로 맛을 봤으며
  - 결국 이 코드 예제를 활용해서 내가 직접 .JSON 파일을 열어보기도 하였다.
- 리스트에 요소를 추가하는 법 역시 다시 복습한 느낌이다.
  - 귀찮아서 `list.append(i)` 코드를 많이 사용했었는데
  - `list += [i]` 이런식으로도 가벼운 느낌으로 리스트에 요소를 추가할 수 있다는 것을 학습하였다.



# 중요 코드

### JSON

```python
import json
movie_json = open('data/movie.json', encoding='UTF8')
movie_dict = json.load(movie_json)
```

- json을 import 해야 사용가능한 것 같다.
- `open`이라는 명령어를 통해 json파일을 열어야하는 것 같다
  - 이 때 앞에 있는 인자는 상대 주소를 의미한다.
- json 객체를 `json.load`를 통해 다시 객체에 저장한다.
  - 비로소 json 파일 안에 쓰여진 자료들을 사용할 수 있게 된다.
  - 기본적으로 딕셔너리 구조였다.

```python
#고급기술?
for movie in movies:
        # id 저장
        id = movie['id']
        # 해당 id에 해당하는 json 파일 열기
        movie_json = open(f'data/movies/{id}.json', encoding='UTF8')   # ==> 주목
        # 상세정보 json파일을 딕셔너리 객체로 저장
        movie_dict = json.load(movie_json)
        movie_release_date = movie_dict["release_date"]
        # 개봉한 달이 몇 달인지 보기 위해 문자열 슬라이싱
        movie_release_month = movie_release_date[5:7]
        # 만약 해당 영화가 12월에 개봉되있으면 제목리스트 추가
        if movie_release_month == '12':
            title_list += [movie_dict['title']]

# 주목
# 해당 id를 저장해서 그 id의 제목을 갖고 있는 json파일을 여는법이다.
```



### Project 내용

### a

- 단순하게 필요한 내용만 새로운 딕셔너리 객체에 저장했다.
- 이 때 인자로 받은 movie는 json파일의 딕셔너리 객체이다.

### b

- 영화 정보가 있는 딕셔너리 객체와, 장르 아이디에 맞는 장르 네임이 있는 딕셔너리 객체 2개를 인자로 받는다.
- 이 때 영화 정보가 있는 딕셔너리 객체에서 영화의 장르 id를 가져와서
- 그 장르 id에 해당하는 장르 네임을 뒤에 있는 객체를 이용해서 살펴본다.
- 장르가 여러개 이기 때문에 장르를 순회하는 for문 하나
- 그 장르 id에 맞는 장르 name을 찾기 위해 장르 객체를 순회하는 for문 하나
- 총 2개의 for문을 사용했다.

### c

- a와 b는 영화 하나의 딕셔너리 객체를 인자로 받았는데
- c는 영화 20개의 딕셔너리 객체가 저장된 리스트 객체를 인자로 받았다.
- 코드 자체는 b와 동일한데
-  `for moive in moives` 를 통해 moives 리스트 객체 속에 있는 딕셔너리 하나하나를 moive로 순회한다.

### d

- 여기서 처음으로 json을 활용하는 코드를 직접 작성해보았다.
- ` movie_json = open(f'data/movies/{id}.json', encoding='UTF8')`을 이용해서 해당 json 파일을 열고
- `movie_dict = json.load(movie_json)`을 이용해서 json 파일내의 정보(딕셔너리 객체)를 저장한다.
- {id}는 f포맷팅으로 작성했는데 id는 별도로 영화리스트 안의 영화 하나하나 객체의 id를 다음 것이다.
- 이번 프로젝트에서는 영화 id에 해당하는 이름의 json파일에 영화 상세정보가 저장되어 있어서 이를 활용했다.
- 영화 20개 중에 최고수익을 찾아야하기 때문에 영화리스트를 돌 때 상세정보의 수익을 비교해서 가장 큰 값일 때의 영화 제목을 저장하여, 그것을 for문 끝난 다음에 반환한다.

### e

- 기본 맥락은 d와 동일하다.
- 다만 개봉일자가 년/월/일 형식으로 저장되어 있기 때문에
- 나같은경우는 문자열 슬라이싱을 통해 월 부분만 추출해서
- 이를 '12' (문자열 12이다.)와 같을 때 영화 제목을 새로운 리스트에 저장하여
- for문이 끝나고 그 리스트를 반환하였다.
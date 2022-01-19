## 22.01.19

### 함수를 왜 사용할까?

- Decomposition
  - 기능(로직)을 분해하고 재사용 가능하게 만들기 위해
- Abstraction
  - 복잡한 내용을 모르더라도 사용할 수 있도록(블랙박스) 재사용성과 가독성, 생산성을 높여줌

# 함수 기초

### 함수(Function)의 정의

- 특정한 기능을 하는 코드의 조각
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

### 사용자 함수

- 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

```python
def function_name(parameter):
    # code blcok
    return returning_value
```

### 함수 기본 구조

- 선언과 호출
  - def 키워드 활용
  - 들여쓰기를 통해 Function body를 작성
    - Docstring은 함수 바디 앞에 선택적으로 작성 가능
    - 작성 시에는 반드시 첫 번째 문장에 문자열 ''' '''
  - 함수는 parameter를 넘겨줄 수 있음
  - 함수는 동작 후에 return을 통해 결과값을 전달함
  - 함수는 함수명()으로 호출
- 입력
- 문서화
- 범위
- 결과값

# 함수의 결과값

### 값에 다른 함수의 종류

- return과 print를 헷갈리면 안된다.

- Void function

  - 명시적인 return 값이 없는 경우, None을 반환하고 종료

    ``` python
    a = print('hello')
    # 일떄 a = None 이다.
    ```

- Value returning function

  - 함수 실행 후, return 문을 통해 값 반환

  - return 시 함수 종료

  - 두 개 이상의 값을 반환 가능

    - 정확하게는 튜플 객체 하나로 반환 되는 것

      ```python
      def m(x, y):
          return x - y, x + y
      # 반환값으로 튜플 객체 (x-y, x+y)가 반환된다.
      ```

### 값 반환 외의 return문의 용도

- 함수 빠져나가기

# 함수의 입력

### Parameter와 Argument

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자(이름)

- Argument : 함수를 호출할 때 넣어주는 값

  - 필수 Argument : 반드시 전달되어야 하는 argument

  - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

  - Positional Argument 

    - 기본적으로 함수 호출 시 Argumnet는 위치에 따라 함수 내에 전달됨
    - add(2, 3)

  - Keyword Argument

    - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음

    - Keyword Argument 다음에 Positional Argument를 활용할 수 없음

      - 키워드를 지정하는 순간 위치가 이미 의미가 없어졌다.

      ```python
      add(y=2, x=1)	#정상처리
      add(2, y=5)		#정상처리
      add(x=1, 5) 	#에러
      ```

- Default Argument Values

  - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

  - 정의된 것보다 더 적은 개수의 argument들로 호출 될 수 있음

    ```python
    def add(x, y=0):
        return x + y
    add(2) #호출 가능
    ```

### 정해지지 않은 여러 개의 Arguments 처리

- Positional Arguments Packing/Unpacking 연산자(*)

  - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용

- keyword Arguments Packing/Unpacking 연산자(**)

  - 함수가 임의의 개수 Argument를 keyword Argument로 호출될 수 있도록 지정
  - Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

  ```python
  def add(*args):		  # args에 하나를 넣어도 튜플로 args 받음, 이름은 복수형 s 붙이는 것이 좋다
      for arg in args:
          print(arg)
  add(2)
  add(2,3,4,5)
  
  def family(**kwargs):
      for key, value in kwargs:
          print(key, ":", value)
  family(father = 'john', mother = 'jane', me = 'john jr.')
  
  def example(**args, a):
      # 아예 정의조차 안됨
      # keyword argument로 넣을 수 조차 없어서 
  def ex(*args, a)
  ex(1,2,3,4, a=5) # 이렇게하면 실행가능하다
  ```

### 함수 정의 주의 사항

```python
def greeting(name = 'john', age):
# 에러발생
# 기본 argument 값을 가지는 argument 다음에 기본값이 없는 argument로 정의할 수 없음
# 위치 박살
```

# 함수의 범위

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global space로 구분
- Scope
  - global : 코드 어디에서든 참조할 수 있는 공간
  - local : 함수가 만든 scope, 함수 내부에서만 참조 가능
- Variable
  - global : global scope에 정의된 변수
  - local : local scope에 정의된 변수

### 변수 수명주기

- 변수는 각자의 수명주기가 존재
  - bulit-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때 까지 유지
  - local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때 까지 유지

### 이름 검색 규칙

- LEGB 규칙에 따름
  - Local scope : 함수
  - Enclosed s : 특정 함수의 상위 함수
  - Gloabl s : 함수 밖의 변수, import 모듈
  - Buli-in scope : 파이썬 안에 내장 되어 있는 함수 또는 속성

### global문

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
- global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 ㅅ ㅜ없음
- global에 나열된 이름은 parameter, for, 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야함

### nonlocal

- global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함
- global과는 달리 이미 존재하는 이름과의 연결만 가능함

# 함수의 문서화

- 함수나 클래스의 설명
- 쥬피터 노트북에서 함수에 커서를 놓고 shift + tab
- 좋은 함수와 parameter 이름을 짓는 방법
  - 상수 이름은 영문 전체를 대문자
  - 클래스 및 예외의 이름은 각 단어의 첫글자만 영문 대글자
  - 이외 나머지는 소문자 또는 밑줄로 구분한 소문자 사용 -> 함수
- 스스로를 설명
- 약어 사용을 지양

# 함수 응용

- 내장함수
  - 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

### map

- map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수 적용하고 그 결과를 map object로 반환

```python
n, m = map(int, inpurt().split())
# function에는 각 요소에 적용하고 싶은 이름을 집어넣는 것
```

### filter

- filter(function, iterable)
- 순회 가능한 데이터 구조의 모든 요소에 함수 적용하고, 그 결과가 True인 것들을 filter object로 반환

### zip

- zip(*iterables)
- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

### lambda 함수

- 람다 함수
  - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용가능

```python
triangle_area = lambda b, h : 0.5 * b * h
triangle_area(5, 6)
# 람다 없이 필터
def odd(n):
    return n % 2
result = filter(odd, numbers)
# 람다 필터
result = filter(lambda x: x % 2, numbers)
```

### 재귀함수

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음 (ex 점화식)
  - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
factorial(4)
```

- 주의 사항
  - 재귀 함수는 base case에 도달할 때 까지 함수를 호출함
  - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
  - 파이썬에서 최대 재귀 높이(maximum recursion depth)가 1,000번으로 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

- 반복문과 재귀 함수 비교
  - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함
  - 재귀 호출은 변수 사용을 줄여줄 수 있음
  - 재퀴 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림

# 모듈과 패키지

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지를 포함

```python
import module
pprint.pprint(a)
from module import var, function, Class
pprint(a)
from module import *
from package import module
from package.module import var, function, Class
from package.module import very_long_name as vln
# vln으로 very_long_name 대신 사용 가능
```

# 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장함수

### 파이썬 패키지 관리자(pip)

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

```bash
$ pip install SomePackage
$ pip uninstall SomePackage
$ pip list	# 패키지 목록 및 특정 패키지 정보
$ pip show SomePackage

$ pip freeze 
#설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
#해당하는 목록을 requirements.txt(관습)으로 만들어 관리함
```

- 패키지 관리하기

  - 아래의 명령어들을 통해 패키지 목록을 관리하고 설치할 수 있음
  - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

  ```bash
  $ pip freeze > requirements.txt # 텍스트 파일로 저장
  $ pip install -r requirements.txt # 텍스트 파일로 저장된 것을 설치
  # 협업할 때 설치된 패키지를 동일하게 맞춰주기 위해 사용!
  ```

# 사용자 모듈과 패키지

- 패키지는 여러 모듈/하위 패키지로 구조화
  - 활용 예시 : package.module
- 모든 폴더에는 `__init__.py`를 만들어 패키지로 인식
  - 3.3부터는 안해도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 생성하는 것을 권장

# 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

### venv

- 가상 환경을 만들고 관리하는데 사용하는 모듈 (파이썬 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경(패키지 집합 폴더 등)이 있고
  - 실행 환경(ex bash)에서 가상환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리/사용함

```bash
$ python -m venv <폴더명> #해당 디렉토리에 별도의 파이썬 패키지가 설치됨
$ source venv/Scripts/activate #가상환경 활성화
```



# 유용한 패키지와 모듈


































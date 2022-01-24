## 22.01.24

# 순서가 있는 데이터 구조

## 문자열

- 모든 문자는 str 타입
- 문자열을 묶을 때 동일한 문장부호를 활용(PEP8에서 하나의 문장부호를 선택해 사용, " ", ' ')
- immutable 하다.

### 문자열 조회/탐색 및 검증 메소드

```python
s.find(x)	# x의 첫 번째 위치를 반환, 없으면 -1을 반환
s.index(x)	# x의 첫 번째 위치를 반환, 없으면 오류 발생
s.isalpha()	# 알파벳 문자 여부, 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)
s.isupper() # 대문자 여부
s.islower()	# 소문자 여부
s.istitle() # 타이틀 형식 여부
```

### 문자열 변경 메소드 (변경될 문자열을 반환)

```python
s.replace(old, new[, count])	# 바꿀 대상 글자를 새로운 글자로 바꿔서 반환, 
								# count는 몇번할 것인가 선택
s.strip([chars])				# 공백이나 특정 문자를 제거, 지정하지 않으면 공백 제거
s.lstrip, s.rstrip				# 왼쪽 오른쪽 제거
s.split([chars])				# 공백이나 특정 문자를 기준으로 분리, 리스트로 반환
'separator'.join([iterable])	# 구분자로 iteralbe을 합침
								# iterable 요소를 쪼개서 그 뒤에 'separator'을 붙임
    							# 이때 itreable은 문자열이여 한다.
        						# map(str, iterable)
s.capitalize()					# 가장 첫 번째 글자를 대문자로
s.title()						# '나 공백 이후를 대문자로
s.upper()						# 모두 대문자
s.lower()						# 모두 소문자
s.swapcase()					# 대<->소문자 변경하여
```

## 리스트

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
- 가변자료형
- 항상 대괄호 형태로 출력

### 리스트 메소드

```python
L.append(x)		# 리스트 마지막에 항목 x를 추가
L.insert(i, x)	# 리스트 인덱스 i에 항목 x를 삽입
L.remove(x)		# 리스트 가장 왼쪽에 있는 항목(첫번째) x를 제거
				# 항목이 존재하지 않을 경우, ValueError
L.pop()			# 리스트 가장 오른쪽에 있는 항목을 반환 후 제거
L.pop(i)		# 리스트의 인덱스 i에 있는 항목을 반환 후 제거
L.extend(m)		# 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)
L.index(x, start, end)	# 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
L.reverse()		# 순서를 반대로 뒤집음 (정렬 x)
L.sort(...)		# 리스트를 정렬(매개변수 이용가능)
L.count(x)		# 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환
```

- sorted(list) vs list.sorted()

```python
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result)	# 정렬된 리스트, None 반환
result = sorted(numbers)
print(numbers, result)	# 원래 리스트, 정렬된 리스트 반환
```



## 튜플

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
- 불변자료형
- 항상 소괄호 형태로 출력
- 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메소드만을 지원
- 리스트 메소드 중 항목을 변경하는 메소드들을 제외하고 대부분 동일



# 순서가 없는 데이터 구조

## Set (셋)

- 순서없이 0 개 이상의 해시가능한 객체를 참조하는 자료형
- 해시 가능한 객체(불변자료형)만 담을 수 있음
- 담고 있는 객체를 삽입, 변경, 삭제 가능 -> 가변자료형
- 수학에서의 집합과 동일한 구조를 가짐
  - 집합 연산이 가능
  - 중복된 값이 존재하지 않음

### set 메소드

```python
s.add(x)	# 항목 x가 셋 s에 없다면 추가
s.update(*other)	# 여러 값을 추가
s.pop()		# 셋s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
			# set이 비어 있을 경우, KeyError
s.remove(s)	# 항목 x를 셋 s에서 삭제
			# 항목이 존재하지 않을 경우, KeyError
s.discard(elem)	# 셋에서 삭제하고, 없어도 에러가 발생하지 않음    
```

## 딕셔너리(Dictionary)

- 순서 없이 키-값 쌍으로 이뤄진 객체를 참조하는 자료형
- 딕셔너리의 키(key)
  - 해시가능한 불변 자료형만 가능
- 각 키의 값(values)
  - 어떠한 형태든 관계 없음

### 딕셔너리 메소드

```python
d.get(k, v)		# 키 v의 값을 반환하는데, 키 K가 딕셔너리 d에 없을 경우 None, v를 반환
d.pop(k[, default])	# key가 딕셔너리에 있으면 제거하고 해당 값을 반환
					# 그렇지 않으면 default를 반환, default값이 없으면 KeyError
d.update(apple = '사과') # apple 키에 접근하여 '사과'라는 값으로 덮어씀
```

# 얕은 복사와 깊은 복사

### 할당

- 대입연산자 =
  - 리스트 복사 확인하기
  - 대입 연사자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
  - 해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향

```python
A = [1, 2, 3]
A_copy = A
A_copy[0] = 5
print(A[0], A_copy[0])	# 5, 5 출력
```

### 얕은 복사(shallow copy)

- Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)

```python
a = [1, 2, 3]
b = a[:]
b = list(a)
b[0] = 5
print(a[0], b[0])	# 1, 5 출력
```

- 주의사항
  - 복사하는 리스트의 원소가 주소를 참조하는 경우

### 깊은 복사(deep copy)

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy,deepcopy(a)
b[2][0] = 0
print(a, b)
#[1, 2, ['a', 'b']]
#[1, 2. [0, 'b']]
```





# 에러 / 예외 처리

- 조건문을 사용할 때 모든 조건을 커버하는가?
- 반복문이 원하는 횟수만큼 반복하는가? 반복문 값 변경이 원하는대로 진행이 되는가? (진입, 결과)
- while문의 종료조건이 제대로 설정이 되어 있는가
- 함수의 호출이 제대로 되었는지, 파라미터를 제대로 넘겼는지, 결과가 올바른지 // type

### 디버깅

- print 함수 활용
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
- Python tutor 활용(단순 파이썬 코드인 경우)

- 에러 메시지가 발생하는 경우
  - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
    - 전체 코드를 살펴봄
    - 휴식을 가져봄
    - 누군가에게 설명해봄

## 에러와 예외

### 문법에러 (Systax Error)

- SysntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때 (parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호 ^를 표시
- EOL (End of Line)
  - 따옴표가 제대로 안됨
- EOF (End of File)
  - 괄호가 제대로 안닫힘

### 예외

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외라고 부름
- 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력됨
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음
- ZeroDivisionError
- NameError : namespace 상에 이름이 없는 경우
- TypeError : 타입 불일치, argument 누락&초과&불일치
- ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
- IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
- KeyError : 해당 키가 존재하지 않는 경우
- ModuleNotFoundError : 존재하지 않는 모듈을 import 하는 경우
- ImportError : Module은 있으나 존재하지 않는 클래스 / 함수를 가져오는 경우
- KeyboardInterrupt : 임의로 프로그램을 종료하였을 때 (무한 루프 등)
- IndentationError : Indentation이 적절하지 않는 경우 (띄어쓰기 오류)

## 예외 처리

- try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try 문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
- except 문
  - 예외가 발생하면, except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

```python
try:
    num = input()
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
```

```python
try:
    num = input()
    print(100 / int(num))
except ValueError:
    print('숫자를 넣어주세요')
except ZeroDivsionError as err:	# as 키워드 활용하여 원본 에러 메시지를 사용할 수 있음
    print(f'{err}, 0으로 나눌 수 없습니다')
except:
    print('에러가 뭔지 모르겠는데 에러발생')
```

- else
  - try 문에서 예외가 발생하지 않으면 실행함
- finally
  - 예외 발생 여부와 관계없이 항상 실행함

## 예외 발생시키기

- raise를 통해 예외를 강제로 발생

  ```python
  raise ValueError('값 에러 발생')
  ```

- assert를 통해 예외를 강제로 발생

  - assert는 상태를 검증하는데 사용되며, 무조건 AssertionError가 발생
  - 일반적으로 디버깅 용도로 사용

  ```python
  assert len([1, 2]) == 1, '길이가 1이 아닙니다'
  # , 전에 있는 표현식이 False인 경우 메시지 출력
  ```

  






























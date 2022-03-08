### 변수

- 선언할 때 모든 타입과 관계없이 var keyword를 사용한다.

- 자바스크립트는 동적 타입 언어
  - 변수의 타입 지정없이 값이 할당되는 과정에서 자동으로 변수의 타입이 결정
  - `>>`같은 변수에 여러 타입의 값을 할당 가능
- 낙타 표기법 사용
  - 자바랑 동일하다
- 키워드 공백문자 포함, 숫자로 시작 x
- 특수 문자 _와 $ 허용
- 타입
  - 원시 타입
    - 숫자형
      - number
    - 문자열형
      - string
    - 불린형 : 값이 있으면 true 없으면 false(null, 비어 있는 문자열, undefined, 0)
      - boolean
    - undefined : 변수가 선언 되었지만 초기화가 되지 않을 경우
      - undefined 
    - null : 값이 존재하지 않는 경우
      - object
    - 아래에 있는거 typeof 출력 값이다.
  - 객체 타입

- 언더플로우, 오버플로우, 0으로 나누는 연산에 대해 예외를 발생시키지 않는다
  - Infinity
    - 무한 대를 나타내는 상수, 어떠한 수를 0 으로 나누거나 Infinity를 어떠한 수로 사칙연산한 결과
  - NaN (Not a Number) 
    - 계산식의 결과가 숫자가 아님을 나타내는 상수
- 문자열
  - ` 백틱 사용 가능
    - 요게 파이썬의 f포맷팅과 비슷하게 사용할 수 있다.
    - 변수에 접근할 때는 ${변수} 로 사용한다.
- 호이스팅
  - var 선언문이나 function 선언문 등 모든 선언문이 해당 Scope의 처음으로 옮겨진 것처럼 동작하는 특성
    - 즉 자바스크립트는 모든 선언문이 선언되기 이전에 참조가 가능
  - 변수의 생성
    - 선언 단계 : 변수 객체에 변수를 등록
    - 초기화 단계 : 변수 객체에 등록된 변수를 메모리에 할당. undefinded로 초기화됨
      - 여기까지 한번에 이루어짐
    - 할당 단계 : 변수에 실제 값을 할당

- 상수
  - ECMAScript 이전까지는 상수 표현을 지원하지 않음
    - 변수 명명 규칙을 다르게 사용
    - 상수의 표기법은 모든 문자를 대문자를 사용하고 단어 사이는 `_`로 표기
    - 그러나 변경이 가능해짐
  - 이후 const Keyword가 추가되어 상수를 지원
- let, const
  - 선언위치
    - 해당 스코프
  - 재선언
    - 불가능
  - var는 전역 스코프, 재선언 가능

### 연산자

- deleter
  - 프로퍼티를 제거
- in
  - 프로퍼티가 존재하는 지 확인

### 객체

- 전역 객체를 제외한 자바스크립트 객체는 프로퍼티를 동적으로 추가하거나 삭제 가능
- 키와 값으로 구성된 프로퍼티 들의 집합
- 일급 객체이므로 값으로 사용할 수 있다. 따라서 프로퍼티의 값으로 함수를 사용 가능

- 생성
  - 객체 리터럴
  - Object 생성자 함수
  - 생성자 함수

- 접근
  - `.`을 이용하거나 대괄호([ ])를 사용해서 속성 값에 접근, 대괄호 내에 들어가는 프로퍼티 이름은 반드시 문자열이어야 한다.
  - 객체에 없는 속성에 접근하면 undefined를 반환
  - 속성명에 연산자가 포함된 경우 [] 표기법만 접근 가능
- 속성 값 변경, 추가, 제거
  - 객체에 값을 할당하는 속성이 없을 경우 그 속은 추가됨
  - delete 연산자를 이용하여 속성 제거
- 객체는 복사되지 않고 참조된다.

### 함수

- 일급 객체이다
  - 함수를 변수 객체 배열 등에 저장할 수 잇고 다른 함수에 전달하는 전달인자(콜백함수) 또는 리턴 값으로 사용가능
- 프로그램 실행 중에 동적으로 생성 가능
- 함수 선언문, 함수 표현식, Function 생성자 함수

- 함수 호이스팅
  - 함수 선언문의 경우 함수 선언의 위치와 솽관없이 코드 내 어느 곳에서든지 호출이 가능
  - 자바스크립트 엔진이 스크립트가 로딩되는 시점에 이를 변수객체에 저장한다.
  - 함수 선언, 초기화 할당이 한번에 이루어진다
  - 함수 표현식의 경우 함수 호이스팅이 아니라 변수 호이스팅이 발생

- 매개변수
  - 타입이 명시되지 않음
  - 매개변수와 전달인자의 개수가 일치하지 않더라도 호출 가능
    - 순서대로 박아 넣는다
- 콜백함수 !!!!!!!!!!!!!!!!
  - 매개변수를 통해 전달되고 전달받은 함수의 내부에서 어느 특정시점에 실행됨
  - 비동기식 처리 모델에서 사용됨
    - 처리가 종료되면 호출될 함수(콜백함수)를 미리 매개변수에 전달하고 처리가 종료되면 콜백함수를 호출

### Window 객체

- alert, comfirm, prompt
  - alert() : 브라우저 알림창
  - confirm() : 브라우저의 확인 취소 선택창
    - if문이랑 같이 쓰인
  - prompt() 브라우저의 입력 창
- navigator
  - userAgent : 브라우저 별로 다르게 처리

- loaction, history
  - location
    - location.href : 프로퍼티에 값을 할당하지 않으면 현재 URL을 조회하고 값을 할당하면 할당 된 URL로 페이지 이동
    - location.reload() : 현재 페이지를 새로고침

- 객체 프로퍼티

### DOM

- elment와 attribute

- 문서객체만들기
  - createElement(tagName) : tag 생성
  - createTextNodE(text : text node 생성
  - appendChild(node) : 객체에 node를 child로 추가

- 객체 속성 설정
  - setArrtibute(name, value)
  - getArrtibute(name)
  - 웹 브라우저가 지원하는 태그의 속성을 사용할 때는 . 으로 사용가능
  - 그렇지 않고 없는 속성을 만들고 싶으면 위 두 함수를 사용해야한다.

- 객체가져오기
  - s 붙고 안붙고 반드시 구별
    - s 안 붙으면 하나만
    - s 붙으면 해당하는 객체의 배열
    - querySelector는 첫번째 element 객체 얻기
    - querySelectorAll 은 모든 element 배열 얻기

### 이벤트

- 자바스크립트를 사용하여 DOM에서 발생하는 이벤트를 감지하여 이벤트에 대응하는 여러 작업 수행
- 이벤트는 일반적으로 함수와 연결이 되고 함수는 이벤트가 발생되기 전에는 실행되지 않다가 이벤트가 발생할 경우 실행 >> 이벤트 핸들러 또는 이벤트 리스너라 한다.
- 종류
  - 인라인 이벤트 핸들러
  - 이벤트 핸들러 프로퍼티 방식
  - addEvantListener

-----------------

## WEBEX

- arrow function

  - 자바에서의 람다식과 유사

    ```html
    <script>
        var print = () => {
            console.log("arrow3");
            console.log("arrow3");
          };
          print();
    
          const add = (a, b) => a + b;
          console.log(add(2, 4));
    </script>
    ```

  - OOP 개념이 아니라서 this 라는 키워드를 제대로 활용할 수 없다.

    - function을 수행하는 객체가 아니라 그 상위 객체를 가르킨다.

    ```html
    <script>
    const obj = {
            num: 5,
            // print: function () {
            //   console.log(this.num);
            // },
            print: () => {
              console.log(this.num);
              console.log(this);
            },
          };
        // 두개의 프린트가 다르게 작용
        // 위의 프린트는 제대로 num을 출력하지만
        // 아래의 프린트는 this가 obj가 아닌 윈도우를 가르킨다.
    </script>
    
    ```

- For 문

  ```html
  <script>
        //string
        let str = "Hello";
        // for
        for (let i = 0; i < str.length; i++) {
          console.log(str[i]);
        }
        // for in key
        for (let key in str) {
          console.log(str[key]);
        }
        // for of
        for (let ch of str) {
          console.log(ch);
        }
  </script>
  ```

- callBy
  - object, 배열 등은 참조형복사
  - 일반형은 값복사

- map, filter

  ```html
  <script>
    //map != Map
          //map return new array
          const lastNames = players.map((player) => player.charAt(0));
          lastNames.forEach((ln) => console.log(ln));
  
          players.map((player) => player.charAt(0)).forEach((ln) => console.log(ln));
          const words = ["aaa", "bbb", "ccc", "ddddd", "ee", "ffffff"];
          const result = words.filter((word) => word.length >= 4);
          console.log(result);
     
  </script>
  ```

- slice, join, reverse

  ```html
  <script>
  //slice
        //return new array
        const nums = [1, 2, 3, 4, 5];
        console.log(nums.slice(2, 3));
  
        //join
        //return new array
        console.log(nums.join("  ")); // default comma
  
        //reverse
        //원본이 변경된다
        const nums2 = nums.reverse();
        console.log(nums2);
        console.log(nums);
      //문자열 반전
      console.warn("");
        const str = "Hello";
        console.log(str.split("").reverse().join(""));
  </script>
  ```

- reduce

  ```html
  <script>
  //reduce
        //배열에서 어떤 계산된 값을 얻고자 할 때
        const nums = [3, 2, 7, 4, 9, 6];
  
        //sum
        let sum = nums.reduce((acc, cur) => (acc += cur));
        console.log(sum);
        //min
        let min = nums.reduce((acc, cur) => (acc = acc <= cur ? acc : cur));
        console.log(min);
        let max = nums.reduce((acc, cur) => (acc = acc >= cur ? acc : cur));
        console.log(max);
  </script>
  ```

  
```html
<script></script>
// 반복적으로 여러개 있을 수 있다.
// 되도록 가장 밑에 넣는 것이 일반적
// 그 전에 선언된 변수가 없으면 오류난다
```

- Using document.write() after an HTML document is loaded, will **delete all existing HTML**:
  - 요즘은 이래서 잘 안쓴다.
- `alert` 와 `console.log`를 많이 쓴다.

- `let` 은 `var` 의 모자란 점을 채우기 위해 나온 녀석 (2015)
  - var는 선언이 뒤에 있어도 오류가 나지 않지만
  - let은 오류가 난다.
    - 블락에 없으면 Uncaught ReferenceError : is not defined
    - 블락에 있으면 ~~ : cannot access 'c' before initialization 에러
    - 블락 전에 선언이 되어 있으면 그거 출력함
      - 단 이때 블락안에 똑같은 let 변수가 선언되면 cannot오류 발생

- 자바스크립트는 한글 변수명 선언이 가능하다.
- `===` 연산자는 타입까지 체크
  - null : object 타입
  - 선언만 한 것 : undefined 타입
  - 타입보는건 typeof
- 자바스크립트 function
  - 일급 객체
  - function 바깥의 변수들은 function 안의 변수들에 접근가능
    - 약간 static 같은 느낌이다..!
    - 안에서 var 로 변수 선언하면 바깥에서 쓸 수 없다. (될 줄 알았는데 안되네)
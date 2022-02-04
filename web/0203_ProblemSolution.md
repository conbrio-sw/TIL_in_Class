### HTML 정의

- Hyper Text Markup Language

### HTML 개념

- 웹 표준을 만드는 곳은 'w3c', 'WHATWG'이다. 주도권은 왓위그에 있다.
- 표를 만들 때에는 반드스 `<th>`를 사용할 필요는 없다.
- 제목 태그는 제목 이외에는 사용하지 않는 것이 좋다. (시멘틱 태그들은 그 의미에 맞게 사용하도록 권장된다.)
- 리스트를 나열하기 위해서는 `ol`, '`ul` 태그를 사용할 수 있다. 각 리스트 아이템들은 `li` 태그를 사용해서 나타낸다.
- HTML의 태그 중에 별도의 닫는 태그가 필요없는 태그도 있다. ('input', 'img')

### CSS 정의

- Cascading Style Sheets

### CSS 개념

- HTML과 CSS는 각자 문법을 갖는 별개의 언어이다.
- 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. (user agent stylesheets)
- 자식 요소 프로퍼티는 부모 프로퍼티의 박스 모델, 포지션은 상속 받지 못한다. (width, height, backgroun-color 등)
- 디바이스마다 화면의 크기가 다른 것을 고려하면 vw vh 등 viewport에 따른 상대 단위가 별도로 존재한다.
- id 값은 유일해야 하므로 중복되어서는 안된다.

### CSS 우선순위

- !important
- Inline style
- id 선택자
- class 선택자
- 요소 선택자
- 소스 순서

### 이미지 경로

```html
<img src="../image/my_photo.png" alt="ssafy">
```

### 하이퍼 링크

```html
<a href="https://www.ssafy.com">
	<img src="..\image\my_photo.png" alt="ssafy">
</a>
```



### nth-child(), nth-of-type()

1. #parent > element: nth-child(n)
   - 부모의 n 번째 자식을 찾고
   - 해당 element를 선택하는데
   - 다른 element 모두 자식으로 선택해서 그 자식들 중에 n 번째를 찾는다.
   - n번째 자식이 선택한 element가 아니라면 스타일이 적용되지 않는다.
2. element: nth-of-thpe(n)
   - 부모의 n 번째 자식을 찾는데
   - 자식 중 element의 n번째를 찾는다.

- 2n, 3n 이런식으로도 사용이 가능하다.
- odd를 넣어도 가능
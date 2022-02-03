# HTML

- 하이퍼텍스트마크업랭귀지
  - Hyper Text
    - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
  - Markup Language
    - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

### 웹 페이지를 작성(구조화)하기 위한 언어

- 모든 사람에게 웹 접근성이 쉬워야한다...!

- 웹 문서에는 표준이 있다.
  - WHATWG가 W3C와의 기술 표준화 주도권 싸움에서 승리
    - (웹 브라우저 보유 기업 vs 학자 느낌..?)
- [Support tables for HTML5, CSS3](https://caniuse.com)
  - 요즘은 표준화가 잘 되서 위 사이트를 그렇게 열심히 찾아볼 필요는 없다.
- HTML로만 만들 수 있는 건 메모장과 똑같음
  - 그것을 깔끔하고 기능을 갖게 해주는 건 브라우저의 일

### HTML 기본구조

- html

  - 문서의 최상위(root) 요소

  - 랭귀지 정보가 들어가 있어, 해당 페이지가 사용자의 언어가 다를 경우 '번역하시겠습니까?'가 뜸

- head

  - 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 요소
  - 예시
    - `<title>`: 브라우저 상단 타이틀
    - `<meta>`: 문서 레벨 메타데이터 요소
    - `<link>`: 외부 리소스 연결 요소(CSS 파일, favicon 등)
    - `<script>`: 스크립트 요소(자바스크립트 파일/코드)
    - `<style>`: CSS 직접 작성

- body

  - 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

- DOM(document object model) 트리

  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드 제공함
  - 2space로 영역 구분하기
    - 몇가지 특수한 태그들 빼면은 되기하는데... 그래도 지켜야됨!

- 요소(element)

  - HTML의 요소는 태그와 내용으로 구성되어 있다.

    ```html
    <h1> contents </h1>
    ```

  - HTML의 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - 태그는 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들
    - br, hr, img, input, link, meta
  - 요소는 중첩(nested)될 수 있음
    - 요소의 중첩을 통해 하나의 문서를 구조화
    - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어질 수 있음

- 속성(attribute)

  - 태그별로 사용할 속성은 다르다.

    ```html
    <a href = "https://google.com"></a>
    a : 링크
    href : 속성명
    구글 : 속성값
    ```

  - 공백없이 사용(속성 끼리 구분할 때만 공백으로 구분), 쌍따옴표 사용

  - 속성을 통해 태그의 부가적인 정보를 설정할 수 있음

  - 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공

  - 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재

  - 태그와 상관없이 사용 가능한 속성들도 있음 (HTML Global Attribute)

    - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스 목록(CSS, JS에서 요소를 선택하거나 접근)
    - data-* : 페이지에 개인 사용자ㅏ 정의 데이터를 저장하기 위해 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 지정
    - tabindex ; 요소의 탭 순서

- 시맨틱 태그

  - HTML5에서 의미론적 요소를 담은 태그의 등장(아무런 기능 안함)
    - 기존 영역을 의미하는 div 태그를 대체하여 사용
  - 대표적인 태그 목록
    - header : 문서 전체나 섹션의 헤더(머리말 부분)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)
  - 설명
    - Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
    - 단순히 구역을 나누는 것 뿐만 아니라 의미를 가지는ㅌ 태그들을 활용하기 위한 노력
    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
    - 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야함

### HTML 구조화

- 텍스트 요소

| 태그      | 설명                                                     |
| --------- | -------------------------------------------------------- |
| `<a></a>` | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성 |
| `<b></b>` |                                                          |
|           |                                                          |
|           |                                                          |
|           |                                                          |
|           |                                                          |

- 그룹 컨텐츠
- table
  - table의 각 영역을 명시하기 위해 `<thead> <tbody> <tfoot>` 요소를 사용
- form
  - `<form>`은 정보(데이터)를 서버에 제출하기 위한 영역
  - 기본속성
    - action : form을 처리할 서버의 URL
    - method : form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
    - enctype : method가 post인 경우 데이터의 유형
      - aplication/x-www-form-urlencoded : 기본값
      - multipart/form-data : 파일전송시 (inut type이 file인 경우)

- input

  - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
  - `<input>` 대표적인 특성
    - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
    - value : form control에 적용되는 값(이름/값 페어로 전송됨)
    - required, readonly, autofocus, autocomplete, disabled 등

- input label

  - label을 클릭하여 input 자체의 초점을 맞추거나 활성화시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
  - `<input>`에 id속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

  ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

- input 유형
  - [치트키](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

# CSS

- Cascading Style Sheets
- 스타일을 지정하기 위한 언어
  - 선택하고, 스타일을 지정한다.

- CSS
  - CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
  - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - 속성(Property) : 어떤 스타일 기능을 변경할 지 결정
    - 값(Value) : 어떻게 스타일 기능을 변경할 지 결정
- CSS 정의 방법
  - 인라인(inline)
  - 내부 참조(embedding) - `<style>`
  - 외부 참조(link file) - 분리된 CSS 파일

- 선택자 유형
  - 기본 선택자
    - 전체 선택자(*), 요소 선택자(태그 들)
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  - 결합자(Combinators)
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
  - 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택잨

- CSS 적용 우선순위
  1. 중요도(importance) - 사용시 주의
     1. !important
  2. 우선순위
     1. 인라인 > id> class, 속성, pseudo-class > 요소, pseudo-element
  3. CSS 파일 로딩 순서

- CSS 상속
  - CSS는 상속을 통해 부모 요소의 속성을 자식에서 상속한다.
    - 속성 중에는 상속이 되는 것과 되지 않은 것들이 있다.
    - 상속 되는 것 예시
      - Text 관련 요소(font, color, text=align), opacity, visibility 등
    - 상속 되지 않는 것 예시
      - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
      - position 관련 요소(position, top/right/bottom/left, z-index) 등

### CSS 기본 스타일

- 크기 단위

  - px(픽셀)
    - 고정적인 단위
  - %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
  - em
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  - rem(root em)
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

  - viewport
    - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
    - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
    - vw, vh, vmin, vmax

- 색상 단위
  - 색상 키워드
    - 대소문자를 구분하지 않음
    - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
  - RGB 색상
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
  - HSL 색상
    - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

- CSS 문서 표현
  - 텍스트
    - 서체, 서체 스타일
    - 자간, 단어 간격, 행간, 들여쓰기 등
  - 컬러, 배경
  - 기타 HTML 태그별 스타일링
    - 목록(li), 표(table)

## Selectors 심화

- 결합자
  - 자손결합자
    - 자식의 자식도 포함
  - 자식결합자
    - 자식만
  - 일반 형제 결합자
    - 형제 요소 중 뒤에 위치하는 요소 모두 선택
  - 인접 형제 결합자
    - 형제 요소 중 바로 뒤에 위치하는 요소 선택

## CSS Box model

- 동그라미가 있다고해더라도 그것이 차지하는 영역은 네모 영역이다.
- 모든 요소는 네모(박스모델)이고,
- 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

- 박스 모델
  - content
    - 글이나 이미지 등 요소의 실제 내용
  - padding
    - 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지는 padding까지 적용
  - border
    - 테두리 영역
  - margin
    - 테두리 바깥의 외부 영역, 배경색을 지정할 수 없다.
    - 상하에 대한 마진은 서로 상쇄한다. 더 큰걸로만 인식한다.
- box-sizing
  - 기본적으로 모든 요소의 box-sizing은 content-box
    - padding을 제외한 순수 contents 영역만을 box로 지정
  - 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
    - 그 경우 box-sizing을 border-box으로 설정

## CSS Display

- 모든 요소는 네모이고, 좌측 상단에 배치

- display에 따라 크기와 배치가 달라진다.

- 대표적으로 활용되는 display

  - display : block
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지한다.
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - display: inline
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지한다.
    - width, height, margin-top, margin-botom을 지정할 수 없다.
    - 상하 여백은 line-height로 지정한다.

  - display: inline-block
    - block과 inline 레벨 요소의 특징을 모두 가짐
    - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
  - display : none
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여하지 않음
    - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만하지 않음

## CSS Position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  -  relative : 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
    - 레이아웃에서 요소 차지하는 공간은 static 일 때와 같음(normal position 대비 offset)
    - 원래 블락을 그대로 차지하고 있음
  - absolute : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 body)
  - fixed : 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - 부모 요소와 관계 없이 viewport를 기준으로 이동, 스크롤 시에도 항상 같은 곳에 위치함

## HTML&CSS

- 크롬 개발자 도구
  - 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
- 주요 기능
  - Elements - DOM 탐색 및 CSS 확인 및 변경
    - Styles - 요소에 적용된 CSS 확인
    - Computed - 스타일이 계산된 최종 결과
    - Event Listeners - 해당 요소에 정용된 이벤트(JS)
  - Sources, Network, Performance, Application, Security, Audits 등
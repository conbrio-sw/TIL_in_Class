# GIT

## 초기 설정

- 최초 한 번만 설정

1. 누가 커밋을 남겼는지 확인할 수 있도록 이름과 이메일을 설정

```bash
$ git config --global user.name ~~# git아 나 설정할건데 전역에 사용자이름
$ git config --global user.email ~~# git아 나 설정할건데 전역에 이메일
```

2. 설정된 내용 확인

```bash
$ git config --global --list #or
$ git config --global -l
```



`add` : 현재 상태를 깃으로 관리하겠다.

`commit` : 현재 상태를 버전으로 만들겠다. 

`push` 깃 허브에는 수정 사항과 원본 파일을 집어넣는다 

## git init

- 현재 작업 중인 **디렉토리**를 **깃**으로 관리

```bash
$ git init #초기화 해당디렉토리에...
```

### 주의사항

- 이미 master로 관리중인 폴더 내에서 **절대 절대 절대 git init 금지**

## git status

- working directory와 Staging Area에 있는 파일들의 현재 상태를 확인
- 상태
  - `Untracked` : git이 관리하지 않는 파일 (한번도 staging area에 올라 간 적이 없음) (깃이 수정사항 하나도 모름)
  - `tracked` : git이 관리하는 파일
    - `Unmodified` : 최신상태
    - `modified` : 수정되었지만 staging area에 반영되기 전
    - `staged` : staging area에 반영된 상태








































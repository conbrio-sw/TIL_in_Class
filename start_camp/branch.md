# branch

## git branch 명령어

- 브랜치 `생성, 삭제, 조회` 명령어

```bash
# 브랜치 조회
$ git branch # 작업하고 있는 브랜치에는 *이 붙음

# 원격 저장소의 브랜치 목록 확인
$ git branch -r #remote

# 브랜치 생성
$ git branch {branch name}

# 브랜치 삭제
# 병합된 (수정 내욕을 합치고 난 후에 삭제 가능)
$ git branch -d {branch name}
# (주의) 병합되지 않은 브랜치 강제 삭제
$ git branch -D {branch name}
```



### git switch

- 현재 브랜치에서 다른 브랜치로 `Head`를 이동시키는 명령어
- `Head`는 현재 브랜치를 가리키는 포인터

```bash
# 다른 브랜치로 이동
$ git switch {다른 브랜치 이름}

# 브랜치를 새로 생성하고 동시에 이동 
$ git switch -c {다른 브랜치 이름}
```



### 주의사항

- git switch 하기 전에 commit 하셨나요?
- 만약 아니라면 에러 발생할 수 있음.



### git merge

```bash
$ git merge dev # 현재 브랜치에 dev브랜치를 병합
#Fast-forward : dev에 있는 변동사항을 가져옴
#머지가 끝나면 더이상 작업을 안할 브랜치라면 삭제

#마스터에 변동사항이 있고 그 이후에 머지할 경우
#:wq 명령어..!
$ git log --oneline --graph

# 같은 파일 수정하고 마지막에 머지하면
# CONFLICT 발생
```



### 주의사항

```bash
$git add . # .은 현재 폴더 -> 상위폴더 커밋하려면 상위폴더에 가서 하면된다.
```
























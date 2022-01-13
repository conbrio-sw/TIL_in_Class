## 22.01.13

### 주의사항

`-` : 약자

`--` : 풀 네임 

# Github

## 회원가입

### 설정 변경

- main 브랜츠를 master 브랜치로 기본값 수정

## 원격 저장소와 로컬 저장소 연결

### Repository 생성

- git remote
- git push



```bash
git remote add origin https://github.com/conbrio-sw/TIL_in_Class.git
#원격 저장소 추가할 껀데, origin 이라는 별명으로 해당하는 주소로 업로드, 처음 한 번만
git push -u orign master #오리진 경로에 마스터에 있는걸 넣겠다.


```



### gitignore

- .gitignore 파일은 .git 폴더랑 같은 위치에 있어야 한다.
- `gitignore.io` 홈페이지에서 편하게 만들 수 있다.
- 깃으로 생성할 때는 확장자 명을 쓰면 안된다.
- 프로젝트를 시작할 때 만들어놓고 작업을 해야한다.

- 원격 저장소에도 파일이 있고, 로컬에도 이미 있고, 이미 트래킹 중인 파일을 로컬에서만 더 이상 추적하지 않도록 설정

  ```bash
  $ git update-index --asume-unchanged {file name}
  ```

  

- 로컬에 있는 파일 변동 추적 멈춤

- 원격 저장소에 해당 파일이 이미 있다면 그 파일 삭제 (원격 저장소에 push할 때 해당 파일 삭제)

```bash
$ git rm ---cached {file name}
```



- 로컬, 원격 저장소 모두 파일 삭제 후 추적 중지

  ```bash
  $ git rm {file name}
  # 그냥 삭제하면 delete 기록이 남음, 이렇게 삭제하면 추적 역시 중지
  ```

  

## gitclone

- 원격저장소에 있는 파일에 
















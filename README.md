# DRF_exercise1


추가

11. 같은 대학 사용자 게시글 모아보기
* API
```
[GET] /board/univ/<str:univ>/
```
* Res
```
HTTP 200 OK

[
    {
        "id": Int,
        "user": Int,
        "title": String,
        "body": String
    }
]
```


12. 페이지네이션 (5개)
community/settings.py
![image](https://github.com/LeeSpect/DRF_exercise1/assets/64893709/c0fc8bcf-d477-48ed-b8fb-fa3f05f61977)
참고: https://velog.io/@jewon119/TIL00.-DRF-Pagination-적용하기

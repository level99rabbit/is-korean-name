# 한국인 이름인지 알려주는 프로그램입니다.


# 설치법
```shell
git clone https://github.com/level99rabbit/is-korean-name
cd is-korean-name
pip install -r requirements.txt
```


# 사용법
1) 훈련시키기
```shell
python train.py
```

2) 사용하기

```shell
python is_korean_name.py "유민정"
"유민정" 은/는 한국인 이름입니다.

python is_korean_name.py "권순선"
"권순선" 은/는 한국인 이름입니다.

python is_korean_name.py "귀도 반 로섬"
"귀도 반 로섬" 은/는 외국인 이름입니다.

python is_korean_name.py "제프 딘"
"제프 딘" 은/는 외국인 이름입니다.
```


# 훈련법
1) `data/names/korean.txt` 에 한국인 이름을 추가합니다.

2) `data/names/non_korean.txt` 에 외국인 이름 추가합니다.

3) 훈련시키기
    ```shell
    cd is-korean-name
    python train.py
    ```

4) `data/trained_classifer.pkl`에 훈련 결과가 저장됩니다.


# 데이터는 어디서 구했나요?
알라딘을 크롤링 했습니다.

한국인 이름 여부는 직접 라벨링 했습니다.


# 한계
1) 글자가 한국인 이름에 자주 쓰이면 한국인 이름이라고 판단합니다.

    ```shell
    python is_korean_name.py "호날두"
    "호날두" 은/는 한국인 이름입니다.
    ```


2) 글자가 외국인 이름에 자주 쓰이면 외국인 이름이라고 판단합니다.

    ```shell
    python is_korean_name.py "이세돌"
    "이세돌" 은/는 외국인 이름입니다.
    ```


3) 영문자 이름은 외국인 이름이라고 판단합니다.

    ```shell
    python is_korean_name.py "Kim Yuna"
    "Kim Yuna" 은/는 외국인 이름입니다.
    ```

# 영어단어 나오면, 한국어 뜻 말하기
words = {
    "apple": "사과",
    "book": "책",
    "orange": "오렌지"
}
words_1 = {
    "glass" : "유리",
    "coffee" : "커피",
    "time" : "시간",
}
count = 0
like = len(words) + len(words_1)
# dictionary -> key,value 를 k,v로 입력 가능
for k,v in words.items():

    x = input(f"{k}  : ").strip()

    if x == v:
        count += 1
        print("정답입니다")
    else:
        print("오답입니다")

print("2라운드 시작")

for k,v in words_1.items():

    x = input(f"{k}  : ").strip()
    if x == v:
        count += 1
        print("정답입니다")
    else:
        print("오답입니다")
x = (count / like)* 100

print(f"{count}개 맞추셨습니다")
print("정답률" f"{x:.3f}%","입니다")
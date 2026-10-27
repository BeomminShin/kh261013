# 이상한 출석 번호 부르기1

# 선생님이 부른 출석번호 N개를 num_list 잘 받아적음
n = input()
x = input()
num_list = x.split()

# 메모장 준비 (배열 만들기)
memo = [0] * 24

# 출석 부른 거 보고 메모장 수정
# for문
for student_num in num_list:

    student_num = int(student_num)
    memo[student_num] = int(memo[student_num]) + 1

# 결과 확인
for x in memo[1:24]:
    print(x, end=" ")

# while문
# i = 0
# while i < len(num_list):
#     print(num_list[i])
#     i += 1

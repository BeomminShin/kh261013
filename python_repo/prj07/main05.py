# 1~10 모든 숫자의 합 출력
#
# result = 0
# for i in range(1,11):
#     result += i
# print(result)


# result = 0
# i = int(input())
# for i in range(1,101):
#     result += i
#     if i % 2 == 1:
#         print(result)
#
n = int(input())
result = 0
for i in range(1,n+1):
    if i % 2 == 0:
        result = result + i
print(result)
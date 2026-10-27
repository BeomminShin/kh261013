# 이상한 출석 번호 부르기2
# while 문
# n = input()
# x = input()
# num_list = x.split()
#
# i = len(num_list) - 1
# while i >= 0:
#     num_list[i]
#     print(num_list[i], end=" ")
#     i -= 1

# for 문
n = input()
x = input()
num_list = x.split()

# for i in range(9, -1, -1):
for i in range(len(num_list)-1, -1, -1):
    print(num_list[i], end=" ")

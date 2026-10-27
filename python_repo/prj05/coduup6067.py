# n = int(input())
#
# if n<0:
#     if n%2==0:
#         print(A)
#     else:
#         print(B)

#음수이면서 짝수이면, A
#음수이면서 홀수이면, B
#양수이면서 짝수이면, C
#양수이면서 홀수이면, D
x = int(input())

if x < 0:
    if x % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if x % 2 == 0:
        print("C")
    else:
        print("D")
# tuple
print("===== tuple =====")

x = 10,20,30

print(x[1])
print(len(x)) # 튜플 안에 있는 갯수
print(10 in x) # 튜플 안에 10이 있는지 확인
# x[0] = 11 # 튜플은 수정 불가능이라 재할당 x
print(x[0:3])
# print(type(x))
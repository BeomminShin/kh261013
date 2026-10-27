# dictionary
# {}사용 key:value 묶음으로 쓸 것
x = {
    "name": None,
    "atk": 10,
    "hp": 100
}
print(x)

x["hp"] = 200

print(x["name"])
print(x.get("atk"))  # x[]과 다르게 x.get()은 에러가 안 뜨고 None이 뜸
print(x["hp"])

print("atk" in x)

print(type(x))

for elem in x.items():
    print(elem)
    print(type(elem))

# print(x.keys()) # x안에 있는 모든 key 꺼내기
# print(type(x.keys()))
# print(x.values()) # x안에 있는 모든 value 꺼내기
# print(type(x.values()))
# print(x.items()) # x안에 있는 모든 item(구성요소) 꺼내기
# print(type(x.items()))

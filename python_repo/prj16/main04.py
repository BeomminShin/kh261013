class Coffee:
    shop = "파이썬 카페"

    def __init__(self, name):
        self.name = name


a = Coffee("아메리카노")
b = Coffee("라떼")

Coffee.shop = "판다스 카페"

print(a.shop)
print(b.shop)

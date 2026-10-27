def f01(x):
    result = x(100)
    print(result)


f01(lambda num:num+1)
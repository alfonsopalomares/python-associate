def fun(n):
    for i in range(n):
        return i


def fun2(n):
    for i in range(n):
        yield i


print (fun(5))

for v in fun2(5):
    print(v)

def fn(n):
    if n == 1:
        return 1
    else:
        return n**3 + fn(n - 1)

num = int(input("请输入n求1~n的立方和:"))
print(fn(num))
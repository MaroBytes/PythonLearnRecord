my_dict = {'语文': 89, '数学': 92, '英语': 80}
for key, value in my_dict.items():
    print(key)
    print(value)

# for语句表达式
x = 0
y = [x + 4 for x in range(5) if x % 2 == 0]
print(y)

# zip函数
books = ['疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Python讲义']
prices = [79, 69, 89]
for book, price in zip(books, prices):
    print(f'{book}的价格是{price}')

for i in range(0, 3):
    print(f"i的值是:{i}")
    if 1 == i:
        continue
    print("continue后的输出语句")

x = 3
print("%02d" % (x))
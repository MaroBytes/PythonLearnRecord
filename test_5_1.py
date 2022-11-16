# 九九乘法表
for i in range(1, 10):
    # 行循环
    for j in range(1, i + 1):
    # 列循环
        if j == i:
            print('%d x %d = %d' % (j, i, i * j))
        else:
            print('%d x %d = %d' % (j, i, i * j), end=',')

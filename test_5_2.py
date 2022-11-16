# 初始化循环变量
i = 1
num = 0
# 循环判断输入是否为奇数行，若否则继续要求用户输入
while i:
    num = int(input('请输入要打印的行数：'))
    if num % 2 != 0:
        i = 0
    else:
        print('偶数行无法打印，请重新输入')

# 图案内容
DRAW = '*'
# 图案数量
draw_num = 1
for j in range(1, num + 1):

    # 打印上部
    if j < (num + 1) / 2:
        print(' ' * ((num - draw_num) // 2) + DRAW * draw_num)
        draw_num += 2

    # 打印中部
    elif j == (num + 1) / 2:
        print(DRAW * num)
        draw_num -= 2

    # 打印下部
    else:
        print(' ' * ((num - draw_num) // 2) + DRAW * draw_num)
        draw_num -= 2

str_list = [
    '-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# 初始化循环变量
i = 1
num = 0
# 循环判断输入是否为奇数行，若否则继续要求用户输入
while i:
    num = int(input('请输入要打印的字母数：'))
    if num % 2 != 0:
        i = 0
    else:
        print('偶数个无法打印，请重新输入')

# 初始化每行字符及字符间-的个数 步长4
char_num = 1
# 初始化两头的-个数
gan_num = num * 2 - 2
for j in range(1, num * 2):
    # 打印上部
    if j < num:
        temp_num = num
        for k in range(1, num * 3 + 2):
            if k <= gan_num:
                print(str_list[0], end='')
            elif k >= gan_num + 1 and k <= (char_num + 1) // 2 + gan_num:
                if k % 2 != 0:
                    print(str_list[temp_num], end='')
                    if k != (char_num + 1) // 2 + gan_num:
                        temp_num -= 1
                else:
                    print(str_list[0], end='')
            elif k > (char_num + 1) // 2 + gan_num and k <= char_num + gan_num:
                if k % 2 != 0:
                    temp_num += 1
                    print(str_list[temp_num], end='')
                else:
                    print(str_list[0], end='')
            else:
                print(str_list[0], end='')
        gan_num -= 2
        print('')
        char_num += 4

    # 打印中部
    elif j == num:
        # 初始化字符下标变量
        temp_num = num
        for k in range(1, char_num + 1):
            if k % 2 == 0:
                print(str_list[0], end='')
            elif k <= (char_num + 1) / 2:
                print(str_list[temp_num], end='')
                if k != (char_num + 1) / 2:
                    temp_num -= 1
            else:
                temp_num += 1
                print(str_list[temp_num], end='')
        print('')
        gan_num += 2

    # 打印下部
    else:
        char_num -= 4
        temp_num = num
        for k in range(1, num * 3 + 2):
            if k <= gan_num:
                print(str_list[0], end='')
            elif k >= gan_num + 1 and k <= (char_num + 1) // 2 + gan_num:
                if k % 2 != 0:
                    print(str_list[temp_num], end='')
                    if k != (char_num + 1) // 2 + gan_num:
                        temp_num -= 1
                else:
                    print(str_list[0], end='')
            elif k > (char_num + 1) // 2 + gan_num and k <= char_num + gan_num:
                if k % 2 != 0:
                    temp_num += 1
                    print(str_list[temp_num], end='')
                else:
                    print(str_list[0], end='')
            else:
                print(str_list[0], end='')
        gan_num += 2
        print('')

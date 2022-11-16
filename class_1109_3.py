SIZE = 8
# 1.  循环前初始化
array = [[0] * SIZE]  #对二维列表赋初值，并作为第0行
#该写法实质是枚举1个元素，并赋值一个列表变量
#等价于array=[     [ 0, 0, 0, 0, 0, 0, 0 ]      ]

for i in range(SIZE - 1):
    array += [[0] * SIZE]  #逐行增加，建立第1-6行（两个已存在的表相加后合并）
    #SIZE * SIZE的二维列表创建完成

orient = 0  # 该orient代表绕圈的方向
# 其中0代表向下，1代表向右，2代表向左，3代表向上
j = 0  #行标
k = 0  #列标
#循环初始化完成

for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i  #2.  填入确定位置的数值
    # 3.  确定填入方向
    # 如果位于①号转弯线上
    if j + k == SIZE - 1:
        # j>k，位于左下角
        if j > k:
            orient = 1
            # 位于右上角
        else:
            orient = 2
            # 如果位于②号转弯线上
    elif (k == j) and (k >= SIZE / 2):
        orient = 3
        # 如果j位于③号转弯线上
    elif (j == k - 1) and (k <= SIZE / 2):
        orient = 0
        # 4. 根据方向来控制行标、列标的改变
        # 如果方向为向下绕圈
    if orient == 0:
        j += 1
        # 如果方向为向右绕圈
    elif orient == 1:
        k += 1
        # 如果方向为向左绕圈
    elif orient == 2:
        k -= 1
        # 如果方向为向上绕圈
    elif orient == 3:
        j -= 1

        # 5. 采用遍历输出上面的二维列表
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d ' % array[i][j], end="")
    print("")
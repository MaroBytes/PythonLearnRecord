# 冒泡排序
unsort_list = [6, 3, 7, 5, 8, 1, 4, 9, 2, 1, 2, 3]


def bubble_sort(arg_list):
    n = len(arg_list) - 1
    for i in range(n):
        for j in range(n):
            if arg_list[j] > arg_list[j + 1]:
                arg_list[j], arg_list[j + 1] = arg_list[j + 1], arg_list[j]


bubble_sort(unsort_list)
print(unsort_list)




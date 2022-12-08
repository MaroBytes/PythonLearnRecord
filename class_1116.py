# def my_max(x,y):
#     '''比较大小'''
#     print(id(x))
#     x = 10
#     return x if x>y else y

# def say_hi(name):
#     print('===正在执行say_hi()函数===')
#     return name + ',您好！'

# a = 6
# b = 9
# print(id(a))
# result= my_max(x = 2, y = 5)
# print(a)
# print('result =',result)
# print(my_max.__doc__)
# print(say_hi('孙悟空'))


def demo(x, y, z=3, *book, **score):
    print(book)
    print(score)

my_dict = {'1':0}
demo(1, 2, 3, '5', '4', **my_dict)

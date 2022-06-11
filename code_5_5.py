# class Point:
#     x = 15
#     y = 5

#     def __init__(self, x, y):
#         self.y = y
# p = Point(25, 25)
# print(p.x, p.y)

# import numpy as np

# arr3 = np.eye(3)
# print(arr3)

# def repeated(L):
#     return list(set(L))



def universal_sort(seq):
    seq.sort()
    return seq

a = [1,3,4,2,6,5]
print(universal_sort(a))
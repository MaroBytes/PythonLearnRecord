SIZE = 8
# array = [[0] * SIZE] * SIZE
# print(id(array[0][0]==array[1][0]))
array = [[0] * SIZE]
for i in range(SIZE - 1):
    array += [[0] * SIZE]

orient = 0
row = 0
col = 0
for i in range(1, SIZE * SIZE + 1):
    array[row][col] = i
    if row + col == SIZE - 1:
        if row > col:
            orient = 1
        else:
            orient = 2
    elif (col == row) and (col >= SIZE / 2):
        orient = 3
    elif (row == col - 1) and (col <= SIZE / 2):
        orient = 0
    if orient == 0:
        row += 1
    elif orient == 1:
        col += 1
    elif orient == 2:
        col -= 1
    elif orient == 3:
        row -= 1

for i in range(SIZE):
    for j in range(SIZE):
        print("%02d" % array[i][j], end=" ")
    print("")

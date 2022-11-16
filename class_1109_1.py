strList = []
for i in range(10):
    userStr = input('请输入一个字符串：')
    strList.append(userStr)
else:
    print(strList)

strDict = {}
for j in strList:
    strDict[j] = strDict.get(j, 0) + 1
print(strDict)
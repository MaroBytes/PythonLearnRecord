a = int(input("请输入第一个数"))
b = int(input("请输入第二个数"))
c = int(input("请输入第三个数"))
demo = []
demo.append(a)
demo.append(b)
demo.append(c)
demo.sort()
print(demo.pop(),demo.pop(),demo.pop(),sep='\n')
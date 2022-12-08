import os
import shutil

#目标文件夹，此处为相对路径，也可以改为绝对路径
determination = r'C:\Users\MaroBytes\Desktop\Web课程大作业\3'
if not os.path.exists(determination):
    os.makedirs(determination)

#源文件夹路径
path = r'C:\Users\MaroBytes\Desktop\数据库大作业'
folders = os.listdir(path)
for folder in folders:
    dir = path + '\\' + str(folder)
    files = os.listdir(dir)
    for file in files:
        source = dir + '\\' + str(file)
        deter = determination + str(file)
        shutil.copyfile(source, deter)

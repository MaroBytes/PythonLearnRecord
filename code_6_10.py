import pandas as pd
#读取文件
data=pd.read_csv(r"yinyue.csv",encoding="utf-8")
data.columns=('title','author','listen_num','link')
#删除万单位
data['listen_num']=data['listen_num'].str.strip("万").apply(int)
data
#删除重复值
data=data.drop_duplicates()
data.head()

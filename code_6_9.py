from pyheatmap.heatmap import HeatMap
import numpy as np

N = 10000
X = np.random.rand(N) * 255  # [0,255]
Y = np.random.rand(N) * 255
data = []
for i in range(N):
    tmp = [int(X[i]), int(Y[i]), 1]
    data.append(tmp)
heat = HeatMap(data)
heat.clickmap(save_as="1.png")  #点击图
heat.heatmap(save_as="2.png")  #热图

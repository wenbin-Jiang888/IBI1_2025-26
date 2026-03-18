import numpy as np 
import matplotlib.pyplot as plt
N=10
x= np.random.rand(N)  # 生成10个0-1之间的随机数作为x坐标
y= np.random.rand(N)  # 生成10个0-1之间的随机数作为y坐标
plt.scatter(x,y,marker='o')  # 绘制圆形散点图
plt.show()  # 关键：弹出绘图窗口显示结果
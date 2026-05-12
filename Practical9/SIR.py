import numpy as np
import matplotlib.pyplot as plt

# 模型参数
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# 初始状态
S = N - 1
I = 1
R = 0

# 记录数据
S_list = [S]
I_list = [I]
R_list = [R]

# 模拟
for t in range(time_steps):
    # 感染概率：beta * 感染比例
    infection_prob = beta * (I / N)
    # 随机感染
    new_infected = np.random.binomial(S, infection_prob)
    # 随机康复
    new_recovered = np.random.binomial(I, gamma)
    
    # 更新
    S -= new_infected
    I += new_infected - new_recovered
    R += new_recovered
    
    # 保存
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# 绘图
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR.png', format='png')
plt.show()
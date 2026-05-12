import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# 疫苗比例 0%~90%（避免S变负，更合理）
vacc_rates = np.arange(0, 0.91, 0.1)
colors = [cm.viridis(i) for i in np.linspace(0, 1, len(vacc_rates))]

plt.figure(figsize=(6,4), dpi=150)

for idx, v in enumerate(vacc_rates):
    # 核心修复：保证 S 永远 >= 0
    S = max(int((1 - v) * N) - 1, 0)
    I = 1
    R = 0
    
    I_list = [I]
    
    for t in range(time_steps):
        # 关键：如果没有易感者，直接跳过感染计算
        if S <= 0:
            new_infected = 0
        else:
            infection_prob = beta * (I / N)
            new_infected = np.random.binomial(S, infection_prob)
        
        # 康复人数不能超过当前感染人数
        new_recovered = np.random.binomial(I, gamma) if I > 0 else 0
        
        # 更新（保证数值永远合法）
        S = max(S - new_infected, 0)
        I = max(I + new_infected - new_recovered, 0)
        R += new_recovered
        
        I_list.append(I)
    
    plt.plot(I_list, color=colors[idx], label=f'{int(v*100)}%')

plt.xlabel('Time')
plt.ylabel('Infected people')
plt.title('SIR with Vaccination')
plt.legend(title='Vaccination rate')
plt.savefig('SIR_vaccination.png', format='png')
plt.show()
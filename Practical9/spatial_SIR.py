import numpy as np
import matplotlib.pyplot as plt

# 网格大小 100x100
size = 100

# 模型参数（实验要求）
beta = 0.3
gamma = 0.05
time_steps = 100

# 0 = 易感者
# 1 = 感染者
# 2 = 康复者
grid = np.zeros((size, size), dtype=int)

# 随机放一个初始感染者
x, y = np.random.randint(0, size), np.random.randint(0, size)
grid[x, y] = 1

# 8个方向（周围所有邻居）
neighbors = [(-1,-1), (-1,0), (-1,1),
             (0,-1),          (0,1),
             (1,-1),  (1,0), (1,1)]

# 创建画布，画 2行2列 四张图
plt.figure(figsize=(10, 8))
plot_times = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 要画图的时间点

# 开始模拟
for step in range(time_steps + 1):
    # 如果到了要画图的时间，就画图
    if step in plot_times:
        idx = plot_times.index(step) + 1
        plt.subplot(3, 4, idx)
        plt.imshow(grid, cmap="viridis", vmin=0, vmax=2)
        plt.title(f"Time = {step}")
        plt.axis("off")

    # 复制网格 → 最关键！防止边跑边改导致崩溃
    new_grid = grid.copy()

    # 找到所有感染者
    infected_cells = np.argwhere(grid == 1)

    # 遍历每个感染者
    for i, j in infected_cells:
        # 1. 感染周围8个邻居
        for di, dj in neighbors:
            ni = i + di
            nj = j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if grid[ni][nj] == 0:  # 只有易感者才会被感染
                    if np.random.rand() < beta:
                        new_grid[ni][nj] = 1

        # 2. 感染者有概率康复
        if np.random.rand() < gamma:
            new_grid[i][j] = 2

    # 更新成新的状态
    grid = new_grid

# 保存图片
plt.tight_layout()
plt.savefig("spatial_SIR.png", format="png")
plt.show()
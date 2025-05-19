import numpy as np
import matplotlib.pyplot as plt

# 設定參數
mean = [0, 0]
cov = [[1, 0.8],      # 協方差矩陣
       [0.8, 1]]

# 產生 1000 個 jointly Gaussian 樣本
data = np.random.multivariate_normal(mean, cov, size=1000)

# 繪圖
plt.scatter(data[:, 0], data[:, 1], alpha=0.6)
plt.title('Bivariate Gaussian Samples')
plt.xlabel('X1')
plt.ylabel('X2')
plt.axis('equal')
plt.grid(True)
plt.show()
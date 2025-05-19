import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu=0, sigma=1):
    """
    輸入：
        x   : 數值或 numpy array
        mu  : 平均值（預設為 0）
        sigma: 標準差（預設為 1）
    回傳：
        高斯函數的輸出值
    """
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- (x - mu)**2 / (2 * sigma**2))

# 定義 x 範圍
x = np.linspace(-5, 5, 500)

# 設定參數
mu = 0       # 平均值
sigma = 1    # 標準差

# 計算 y 值
y = gaussian(x, mu, sigma)

# 繪圖
plt.plot(x, y, label=f'μ={mu}, σ={sigma}')
plt.plot(x, gaussian(x, mu=0, sigma=0.5), label='σ=0.5')
plt.plot(x, gaussian(x, mu=0, sigma=1), label='σ=1')
plt.plot(x, gaussian(x, mu=0, sigma=2), label='σ=2')
plt.title('Gaussian with different σ')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()
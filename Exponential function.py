import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# 設定參數
lambda_param = 0.5   # rate parameter λ
sample_size = 100000  # 產生的樣本數量

# 產生指數分佈的隨機樣本
samples = np.random.exponential(scale=1/lambda_param, size=sample_size)

# 計算統計值
mean = np.mean(samples)
variance = np.var(samples)

print(f"理論平均值: {1 / lambda_param}")
print(f"模擬平均值: {mean}")
print(f"理論變異數: {1 / (lambda_param ** 2)}")
print(f"模擬變異數: {variance}")

# 繪圖設定
x = np.linspace(0, 5 / lambda_param, 1000)
pdf = expon.pdf(x, scale=1/lambda_param)
cdf = expon.cdf(x, scale=1/lambda_param)

# 繪製直方圖與 PDF
plt.figure(figsize=(12, 5))

# 直方圖 + PDF
plt.subplot(1, 2, 1)
plt.hist(samples, bins=50, density=True, alpha=0.7, label='Samples')
plt.plot(x, pdf, 'r-', lw=2, label='PDF')
plt.title(f'Exponential Distribution (λ={lambda_param})\nPDF & Histogram')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.grid(True)

# CDF 圖
plt.subplot(1, 2, 2)
plt.plot(x, cdf, 'g-', lw=2, label='CDF')
plt.title(f'Exponential Distribution (λ={lambda_param})\nCDF')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
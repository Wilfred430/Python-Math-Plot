import numpy as np
import matplotlib.pyplot as plt

# 頻率範圍
w = np.linspace(0.01, 10, 500)
s = 1j * w

# 例：H(s) = 1 / (s + 1)
H = 1 / (s + 1)

# 計算幅值與相位
magnitude = np.abs(H)
phase = np.angle(H, deg=True)  # 以度為單位

# 畫圖
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(w, magnitude)
ax[0].set_title('Magnitude')
ax[0].set_ylabel('|H(jω)|')
ax[0].grid(True)

ax[1].plot(w, phase)
ax[1].set_title('Phase')
ax[1].set_ylabel('Phase (degrees)')
ax[1].set_xlabel('Frequency (rad/s)')
ax[1].grid(True)

plt.tight_layout()
plt.show()
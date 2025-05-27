import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# 設定長、寬、高
n = 2  # 長
m = 2  # 寬
k = 2  # 高

# 定義長方體的8個頂點
points = np.array([
    [0, 0, 0],
    [n, 0, 0],
    [n, m, 0],
    [0, m, 0],
    [0, 0, k],
    [n, 0, k],
    [n, m, k],
    [0, m, k]
])

# 定義每個面的頂點
faces = [
    [points[0], points[1], points[2], points[3]],  # 底面
    [points[4], points[5], points[6], points[7]],  # 頂面
    [points[0], points[1], points[5], points[4]],  # 前面
    [points[2], points[3], points[7], points[6]],  # 後面
    [points[1], points[2], points[6], points[5]],  # 右面
    [points[0], points[3], points[7], points[4]]   # 左面
]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 畫出每個面
cube = Poly3DCollection(faces, facecolors='lightgreen', edgecolors='k', linewidths=1, alpha=0.7)
ax.add_collection3d(cube)

# 設定座標軸範圍
ax.set_xlim([0, n])
ax.set_ylim([0, m])
ax.set_zlim([0, k])

ax.set_title('(n×m×k)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
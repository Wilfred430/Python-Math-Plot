import numpy as np

# 定義矩陣
A = np.array([[1, 2],
              [3, 4]])

# 檢查行列式是否非零
if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    print("A 的反矩陣為：")
    print(A_inv)
else:
    print("矩陣不可逆！")
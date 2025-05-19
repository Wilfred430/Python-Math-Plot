import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, yv

x = np.linspace(0.01, 20, 500)  # 避免 x=0

plt.plot(x, jv(0, x), label='J₀(x)')
plt.plot(x, jv(1, x), label='J₁(x)')
plt.plot(x, yv(0, x), '-', label='Y₀(x)')
plt.plot(x, yv(1, x), '-', label='Y₁(x)')
plt.legend()
plt.title('Bessel Functions')
plt.grid(True)
plt.show()
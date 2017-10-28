import numpy as np
import matplotlib.pyplot as plt

xs = np.arange(0,2,0.01)
ys = [x**2 - 2*x for x in xs]
plt.plot (xs, ys)
plt.xlim(1,2)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

print("environment is working")
print(x[:5])

plt.plot(x, y)
plt.title("Test Plot")
plt.show()
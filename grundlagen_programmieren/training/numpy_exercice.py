import numpy as np
import matplotlib.pyplot as plt


m = np.zeros((8, 8))
m[0::2, 1::2] = 1
m[1::2, 0::2] = 1

print(m)

m = np.pad(m, 2, constant_values=2)


print("\n")
print(m)


m = np.random.uniform(size=(15,30))

plt.imshow(m)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.linspace(0,20,11)
y=x**2
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(y,x)
plt.subplot(2,2,3)
plt.plot(x,x)
plt.subplot(2,2,4)
plt.plot(x-y,y)

plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.linspace(0,20,11)
y=x**2
plt.plot(x,y,color='brown')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Demo")
plt.show()
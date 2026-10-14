import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.linspace(0,20,11)
y=x**2

fig=plt.figure(figsize=(5,5),dpi=500)
axis1=fig.add_axes([0.55,0.2,0.4,0.4])
axis2=fig.add_axes([0.05,0.2,0.4,0.4])
axis1.plot(x,y)
axis2.plot(y,x)
plt.show()
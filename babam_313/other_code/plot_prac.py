import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,6*math.pi,1000)
y_1=np.sin(x)
y_2=np.cos(x)
plt.plot(x,y_1)
plt.plot(x,y_2)
plt.show()
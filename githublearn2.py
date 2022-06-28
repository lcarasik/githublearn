'''
Author(s): Lane Carasik
Purpose: Teaching Python + Github
'''

#--------------------------------------
# Import modules

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#--------------------------------------
# Define variables

x = np.linspace(0,4,30)
y = x**2

#--------------------------------------
# Plot

k = 1
plt.figure(k)
plt.plot(x,y)

k = k + 1
plt.figure(k)
plt.plot(x,x)

plt.show()
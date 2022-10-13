import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"]=(12,8)
plt.rcParams["font.size"]=16
N = 40
arr = np.round(np.linespace(0,1000,N),0)
np.random.seed(0)
np.random.shuffle(arr)

fig,ax = plt.subplots()
# arange(start,stop,step size)
ax.bar(np.arange(0,len(arr),1),arr)

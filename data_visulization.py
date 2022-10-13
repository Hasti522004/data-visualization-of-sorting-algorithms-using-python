import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

'''Python NumPy linspace 

Python NumPy linspace 
example 1 In this section, we will learn about the Python NumPy linspace 
example. 2 This linspace function also creates a sequence of evenly spaced values within a defined interval. 
3 It also gives values in the specified range and the values are evenly space like arange function.
'''

'''
round (float_num, Num_of_decimals) is a built-in function available with python. ...
float_num: the float number to be rounded.
Num_of_decimals: It is the number of decimals to be considered while rounding.
It will return an integer value if the num_of_decimals is not given and a float value if the num_of_decimals is given.
'''

'''
random.shuffle () shuffles the original list. The original list can be shuffled in place by using random.shuffle ().
random.sample () returns a new shuffled list. The original list remains unchanged.
'''

'''
syntax: seed(n)
Seed function is used to save the state of a random function, 
so that it can generate same random numbers on multiple executions of the code on the same machine 
or on different machines (for a specific seed value). 
if we use seed multiple time with same argument and range is also same then that much value is also same.
'''
class TrackedArray():
    
    def __init__(self,arr):
        self.arr=arr
        self.reset()
    
    def reset(self):
        self.indices=[]
        self.values= []
        self.access_type=[]
        self.full_copies=[]
        
    def track(self,key,access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))    
        
    def GetActivity(self,idx=None):
        if isinstance(idx,type(None)):
            return [(i,op) for (i,op) in zip(self.indices, self.access_type)]
        else:    
            return(self.indices[idx], self.access_type[idx])    
        
    def __getitem__(self,key):
        self.track(key,"get")
        return self.arr.__getitem__(key)
    
    def __setitem__(self,key,value):
        self.arr.__setitem__(key,value)
        self.track(key,"set")
        
    def __len__(self):
        return self.arr.__len__()
        
plt.rcParams["figure.figsize"]=(12,8)
plt.rcParams["font.size"]=16
FPS =30.0
N=40
arr = np.round(np.linspace(0,1000,N),0)
np.random.seed(0)
np.random.shuffle(arr)
arr=TrackedArray(arr)
#fig,ax=plt.subplots()
# ax.bar(np.arange(0,len(arr),1),arr,width=0.8,align="edge",color="GREEN")
'''
method -2
arr = np.round(np.random.randint(0,1000,N),0)
'''

'''
What does subplots () do in matplotlib?
Subplots mean groups of axes that can exist in a single matplotlib figure. 
subplots() function in the matplotlib library, helps in creating multiple layouts of subplots.
It provides control over all the individual plots that are created.
'''

'''
Figure is like a paper that you can draw anything you want
We have to draw a chart in a “cell”, which is Axes in this context
If we’re drawing only one graph, we don’t have to draw a “cell” first, just simply draw on the paper anyway. So, we can use plt.plot(...).
fig,ax=plt.subplots()
here fig is only work as a paper and assume we can devide this page into N equal parts is called axes.
A given figure can contain many Axes, but a given Axes object can only be in one Figure.
'''

'''
arange()
numpy.arange(start,stop,step_size,datatype) #stop is compulsory
The arange() function is used to get evenly spaced values within a given interval.
Values are generated within the half-open interval [start, stop]. 
For integer arguments the function is equivalent to the Python built-in range function, 
but returns an ndarray rather than a list.
'''

'''
ax.bar(x,y,)
'''


#############################################
######     1.insertion short      ###########
#############################################
sorter="Insertion"
t0 = time.perf_counter()
i=1
while(i<len(arr)):
    j=i
    while((j>0)and (arr[j-1]>arr[j])):
        temp=arr[j-1]
        arr[j-1]=arr[j]
        arr[j]=temp
        j-=1
    i+=1
dt = time.perf_counter()-t0     
    
print(f"........{sorter} Sort.........")
print(f"Array Shorted in {dt*1E3:.1f} ms") 
##############################################
    
fig,ax=plt.subplots()
container=ax.bar(np.arange(0,len(arr),1),arr,width=0.8,align="edge",color="RED")
ax.set_xlim([0,N])
ax.set(xlabel="Index",ylabel="Value",title=f"{sorter} sort")
txt = ax.text(0,1000,"")

def update(frame):
    txt.set_text(f" Accesses = {frame}")
    for(rectangle,height) in zip(container.patches,arr.full_copies[frame]):
        rectangle.set_height(height)
        rectangle.set_color("#1f77b4")
        
    idx,op = arr.GetActivity(frame)
    if op == "get":
        container.patches[idx].set_color("red")
    elif op == "set":
        container.patches[idx].set_color("BLUE")        
        
    return(*container,txt)

ani=FuncAnimation(fig,update,frames=range(len(arr.full_copies)),
                  blit=True,interval=1000./FPS,repeat=False)
#container=ax.bar(np.arange(0,len(arr),1),arr,width=0.8,align="edge",color="RED")
plt.show()
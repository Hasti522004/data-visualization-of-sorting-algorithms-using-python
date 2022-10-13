import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

class TrackedArray():
    
    def __init__(self,arr):
        self.arr=arr
        self.reset()
        
    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []    
        self.full_copies = []
    
    def track(self,key,access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))
        
    def GetActivity(self,idx=None):
        if isinstance(idx,type(None)):
            return [(i,op) for (i,op) in zip(self.indices, self.access_type)]
        else:
            return(self.indices[idx],self.access_type[idx])     
        
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
N = 40
arr = np.round(np.linspace(0,1000,N),0)
np.random.seed(0)
np.random.shuffle(arr)

# arange(start,stop,step size)

#############################################
######     1.insertion short      ###########
#############################################

sorter="Insertion"
i=1
while(i<len(arr)):
    j=i
    while((j>0) and (arr[j-1]>arr[j])):
        temp=arr[j-1]
        arr[j-1]=arr[j]
        arr[j]=temp
        j-=1
    i+=1
print(f"........{sorter} Sort.........")        

fig,ax=plt.subplots()
container=ax.bar(np.arange(0,len(arr),1),arr,width=0.8,align="edge")
txt = ax.text(0,1000,"")

def update(frame):
    txt.set_text(f" Accesses = {frame}")
    for(rectangle,height) in zip(container.patches,arr.full_copies[frame]):
        

plt.show()
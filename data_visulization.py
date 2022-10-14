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
######     1.insertion Sort     ###########
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

# plt.show()

#############################################
##########     2.Quick Sort     ###########
#############################################
# sorter="Quick"
# t0 = time.perf_counter()
# i=1
# def quicksort(A, lo, hi):
#     if lo < hi:
#         p = partition(A, lo, hi)
#         quicksort(A, lo, p - 1)
#         quicksort(A, p + 1, hi)


# def partition(A, lo, hi):
#     pivot = A[hi]
#     i = lo
#     for j in range(lo, hi):
#         if A[j] < pivot:
#             temp = A[i]
#             A[i] = A[j]
#             A[j] = temp
#             i += 1
#     temp = A[i]
#     A[i] = A[hi]
#     A[hi] = temp
#     return i

# t0 = time.perf_counter()

# quicksort(arr, 0, len(arr)-1)

# dt = time.perf_counter()-t0     
    
# print(f"........{sorter} Sort.........")
# print(f"Array Shorted in {dt*1E3:.1f} ms") 
##############################################

# plt.show()  
    
#############################################
######     3.Merge Sort     ###########
#############################################
# sorter="Merge"
# t0 = time.perf_counter()
# i=1

# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
 
#     # create temp arrays
#     L = [0] * (n1)
#     R = [0] * (n2)
 
#     # Copy data to temp arrays L[] and R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
 
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
 
#     # Merge the temp arrays back into arr[l..r]
#     i = 0     # Initial index of first subarray
#     j = 0     # Initial index of second subarray
#     k = l     # Initial index of merged subarray
 
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
 
#     # Copy the remaining elements of L[], if there
#     # are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
 
#     # Copy the remaining elements of R[], if there
#     # are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
 
# # l is for left index and r is right index of the
# # sub-array of arr to be sorted
 
 
# def mergeSort(arr, l, r):
#     if l < r:
 
#         # Same as (l+r)//2, but avoids overflow for
#         # large l and h
#         m = l+(r-l)//2
 
#         # Sort first and second halves
#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         merge(arr, l, m, r)
        
# mergeSort(arr, 0, len(arr)-1)        

# dt = time.perf_counter()-t0     
    
# print(f"........{sorter} Sort.........")
# print(f"Array Shorted in {dt*1E3:.1f} ms") 
##############################################    
 
#############################################
######     4.Heap Sort     ###########
#############################################
# sorter="Heap"
# t0 = time.perf_counter()
# i=1
# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2
 
#  # See if left child of root exists and is
#  # greater than root
 
#     if l < n and arr[i] < arr[l]:
#         largest = l
 
#  # See if right child of root exists and is
#  # greater than root
 
#     if r < n and arr[largest] < arr[r]:
#         largest = r
 
#  # Change root, if needed
 
#     if largest != i:
#         (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
#   # Heapify the root.
 
#         heapify(arr, n, largest)
 
 
# # The main function to sort an array of given size
 
# def heapSort(arr):
#     n = len(arr)
 
#  # Build a maxheap.
#  # Since last parent will be at ((n//2)-1) we can start at that location.
 
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
 
#  # One by one extract elements
 
#     for i in range(n - 1, 0, -1):
#         (arr[i], arr[0]) = (arr[0], arr[i])  # swap
#         heapify(arr, i, 0)
        
# heapSort(arr)
        
# dt = time.perf_counter()-t0     
    
# print(f"........{sorter} Sort.........")
# print(f"Array Shorted in {dt*1E3:.1f} ms") 
##############################################  

#############################################
######     5.Bubble Sort     ###########
#############################################
# sorter="Insertion"
# t0 = time.perf_counter()
# i=1
# def bubbleSort(arr):
#     n = len(arr)
#     # optimize code, so if the array is already sorted, it doesn't need
#     # to go through the entire process
#     swapped = False
#     # Traverse through all array elements
#     for i in range(n-1):
#         # range(n) also work but outer loop will
#         # repeat one time more than needed.
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
 
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
#         if not swapped:
#             # if we haven't needed to make a single swap, we
#             # can just exit the main loop.
#             returnz
       
# bubbleSort(arr)        
        
# dt = time.perf_counter()-t0     
    
# print(f"........{sorter} Sort.........")
# print(f"Array Shorted in {dt*1E3:.1f} ms") 
##############################################

#############################################
######     6.Tim Sort     ###########
#############################################
# sorter="Tim"
# t0 = time.perf_counter()

# MIN_MERGE = 16
 
 
# def calcMinRun(n):
#     r = 0
#     while n >= MIN_MERGE:
#         r |= n & 1
#         n >>= 1
#     return n + r
 
# def insertionSort(arr, left, right):
#     for i in range(left + 1, right + 1):
#         j = i
#         while j > left and arr[j] < arr[j - 1]:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1
 
# # Merge function merges the sorted runs
# def merge(arr, l, m, r):
 
#     len1, len2 = m - l + 1, r - m
#     left, right = [], []
#     for i in range(0, len1):
#         left.append(arr[l + i])
#     for i in range(0, len2):
#         right.append(arr[m + 1 + i])
 
#     i, j, k = 0, 0, l
 
#     # after comparing, we merge those two array
#     # in larger sub array
#     while i < len1 and j < len2:
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
 
#         else:
#             arr[k] = right[j]
#             j += 1
 
#         k += 1
 
#     # Copy remaining elements of left, if any
#     while i < len1:
#         arr[k] = left[i]
#         k += 1
#         i += 1
 
#     # Copy remaining element of right, if any
#     while j < len2:
#         arr[k] = right[j]
#         k += 1
#         j += 1
 
 
# # Iterative Timsort function to sort the
# # array[0...n-1] (similar to merge sort)
# def timSort(arr):
#     n = len(arr)
#     minRun = calcMinRun(n) 
#     # Sort individual subarrays of size RUN
#     for start in range(0, n, minRun):
#         end = min(start + minRun - 1, n - 1)
#         insertionSort(arr, start, end)
 
#     # Start merging from size RUN (or 32). It will merge
#     # to form size 64, then 128, 256 and so on ....
#     size = minRun
#     while size < n:
 
#         # Pick starting point of left sub array. We
#         # are going to merge arr[left..left+size-1]
#         # and arr[left+size, left+2*size-1]
#         # After every merge, we increase left by 2*size
#         for left in range(0, n, 2 * size):
 
#             # Find ending point of left sub array
#             # mid+1 is starting point of right sub array
#             mid = min(n - 1, left + size - 1)
#             right = min((left + 2 * size - 1), (n - 1))
 
#             # Merge sub array arr[left.....mid] &
#             # arr[mid+1....right]
#             if mid < right:
#                 merge(arr, left, mid, right)
 
#         size = 2 * size
        
# timSort(arr)         
 
# dt = time.perf_counter()-t0     
    
# print(f"........{sorter} Sort.........")
# print(f"Array Shorted in {dt*1E3:.1f} ms") 
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
# 1. Create an output array.
# 2. Create a min heap of size k and insert 1st element in all the arrays into the heap
# 3. Repeat following steps while priority queue is not empty.
# …..a) Remove minimum element from heap (minimum is always at root) and store it in output array.
# …..b) Insert next element from the array from which the element is extracted. If the array doesn’t have any more elements, then do nothing.





# merge function merge two arrays 
# of different or same length 
# if n = max(n1, n2) 
# time complexity of merge is (o(n log(n))) 
  
from heapq import merge 
  
# function for meging k arrays 
def mergeK(arr,k):
    l = arr[0]
    for i in range(k-1):
        l = list(merge(l, arr[i+1]))
    
    return l
# for printing array 
def printArray(arr): 
    print(*arr) 
  
  
# driver code 
arr =[[2, 6, 12 ],  
    [ 1, 9 ],  
    [23, 34, 90, 2000 ]] 
k = 3
  
l = mergeK(arr, k) 
  
printArray(l) 


# What is the prop of heap?

# Min Heap
# Ans:    1. Every child is greater than his parent
#         2. Although heaps look like a tree, it looks like an array. For the k th element, their cildren is 2k+1 and 2k+2 th elements and the paremt is int(k/2).
        
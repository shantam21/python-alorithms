def bubble_sort(arr):
    n = len(arr)
    
    already_sorted = True
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]  = arr[j+1], arr[j]
                
                already_sorted = False
        if already_sorted:
            break
    print(arr)

arr = [1,100,9,5,6]

bubble_sort(arr)
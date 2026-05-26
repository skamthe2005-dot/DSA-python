# selection sort

def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]



arr=[20,40,10,15,30]
selection_sort(arr)
print(arr)
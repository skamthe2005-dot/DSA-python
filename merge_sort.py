# merge sort

def merge_sort(arr,l,m,h):
    left=arr[l:m+1]
    right=arr[m+1:h+1]
    i=0
    j=0
    k=l
    while j<len(left) and i<len(right):
        if left[j]<right[i]:
            arr[k]=left[j]
            k+=1
            j+=1
        else:
            arr[k]=right[i]
            k+=1
            i+=1
    while i<len(right):
        arr[k]=right[i]
        k+=1
        i+=1
    while j<len(left):
        arr[k]=left[j]
        k+=1
        j+=1
    

def merge(arr,low,high):
    if low<high:
        mid=(low+high)//2
        merge(arr,low,mid)
        merge(arr,mid+1,high)
        merge_sort(arr,low,mid,high)

arr=[20,40,10,15,30]
merge(arr,0,4)
print(arr)


# hoare's quick sort algorithm

def hoare_partition(arr,l,h):
    pivot=arr[l]
    i=l-1
    j=h+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]

def qsort(arr,l,h):
    if l<h:
        p=hoare_partition(arr,l,h)
        qsort(arr,l,p)
        qsort(arr,p+1,h)


arr=[8,4,7,9,3,10,5]
qsort(arr,0,6)
print(arr)
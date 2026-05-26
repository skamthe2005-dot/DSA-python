# insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        x=arr[i]
        j=i-1
        while j>=0 and arr[j]>x:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=x


arr=[20,40,10,15,30]
insertion_sort(arr)
print(arr)

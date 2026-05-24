# for sorted array
# efficient solution
# by recursive method

def IFO(arr,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if x>arr[mid]:
        return IFO(arr,x,mid+1,high)
    elif x<arr[mid]:
        return IFO(arr,x,low,mid-1)
    elif mid==0 or arr[mid-1]!=arr[mid]:
        return mid
    else:
       return IFO(arr,x,low,mid-1)

arr=[10,10,20,30,30,40,40,50]
print(IFO(arr,40,0,7))




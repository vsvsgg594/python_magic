# Given an array arr. Your task is to find the minimum and maximum elements in the array.

# Note: Return a Pair that contains two elements the first one will be a minimum element 
# and the second will be a maximum.

def get_min_max(arr):
    n=len(arr)
    if n==0:
        return -1
    min_value=arr[0] # 
    max_value=arr[0] # 
    for i in range(0,n):
        if arr[i]<min_value:
            min_value=arr[i]
        if arr[i]>max_value:
            max_value=arr[i]
    return (min_value,max_value)  

arr=[1,2,3,4,5,6,7,8]
ans=get_min_max(arr)
print(ans)
      
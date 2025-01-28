def arraySum(arr):
    n= len(arr)
    if n==0:
        return 0
    sum=0
    for i in range(0,n):
        sum=sum+arr[i]
    return sum
arr=[1,2,3,4]
ans=arraySum(arr)
print(ans)    
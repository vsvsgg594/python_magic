# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.

def largest(arr):
    n=len(arr)
    if n==0:
        return -1
    result=arr[0]
    for i in range(0,n):
        if arr[i]>result:
            result=arr[i]
    return result        
arr=[1,2,3,4,45,5]

ans=largest(arr)
print(ans)  # Output: 45

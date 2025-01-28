# Given an unsorted array arr.
# Find the count of elements less than or equal to the given element x.

# Examples:

# Input: x = 9, arr = [10, 1, 2, 8, 4, 5] 
# Output: 5
# Explanation: The 5 elements are 1, 2, 8, 4 and 5.
def countOfElements(arr,x):
    count=0
    n=len(arr)
    if n==0:
        return -1
    for i in range(0,n):
        if arr[i]<=x:
            count+=1
    return count

ans =countOfElements([1,2,3,4,5],5)
print(ans)  
        

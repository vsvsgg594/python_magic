# Given an array arr[] of positive integers. 
# The task is to return the count of the number of odd and even elements in the array.

# Note: Return two elements where the first one in the count of odd & second one is the count of even.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: 3 2
# Explanation: There are 3 odd elements (1, 3, 5) and 2 even elements (2 and 4).

def countOddEven(arr):
    n=len(arr)
    if n==0:
        return 0
    odd=0
    even=0
    for i in range(0,n):
        if arr[i]%2==0:
            even=even+1
        else:
            odd=odd+1
    return (odd,even)     
arr=[1,2,3,4,5,6,7,8,9]
ans=countOddEven(arr)
print(ans)
       
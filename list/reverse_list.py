# Given an array arr of positive integers. Reverse every sub-array group of size k.

# Note: If at any instance, k is greater or equal to the array size, then reverse the entire array.
# You shouldn't return any array, modify the given array in place.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5], k = 3
# Output: [3, 2, 1, 5, 4]
# Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
# Input: arr[] = [5, 6, 8, 9], k = 5
# Output: [9, 8, 6, 5]
# Explnation: Since k is greater than array size, the entire array is reversed.


def reverseInGroups(arr, k):
    l1=[]
    n = len(arr)
    if n==0 or k>n:
        return -1
    for i in range(0, n, k):  
        l1.extend(arr[i:i+k][::-1])  # 0:0+3==3
    return l1         
ans=reverseInGroups([1,2,3,4,5],3) 
print(ans)       
    
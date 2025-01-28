# Given an array of positive integers arr[], return the second largest element from the array.
# If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
def second_largest_number(arr):
    n=len(arr)
    if n==0:
        return -1
    if n<2:
        return -1
    max=-1
    min=-1
    if arr[0]>arr[1]:
        max=arr[0]
        min=arr[1]
    else:
        max=arr[1]
        min=arr[0]
    for i in  range(2,n):
        if arr[i]>max:
            min=max
            max=arr[i]
        elif arr[i]>min and arr[i]!=max:
            min=arr[i]
    return min

arr=[1,2,3,4,5,6,7,8,9,10]
ans=second_largest_number(arr)
print(ans)
                    
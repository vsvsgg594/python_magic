# Given an array arr[] where no two adjacent elements are same,
# find the index of a peak element. An element is considered to be a peak 
# if it is greater than its adjacent elements (if they exist). If there are multiple 
# peak elements, return index of any one of them. The output will be "true" if the index 
# returned by your function is correct; otherwise, it will be "false".

# Note: Consider the element before the first element
# and the element after the last element to be negative infinity.

# Examples :

# Input: arr = [1, 2, 4, 5, 7, 8, 3]
# Output: true
# Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
def peakElement(arr):
    n = len(arr)
    if n == 0:
        return -1  
    if n == 1:
        return 0  

    for i in range(n):
       
        if (i == 0 or arr[i] >= arr[i-1]) and (i == n-1 or arr[i] >= arr[i+1]):
            return i  

    return -1  


arr = [1, 2, 4, 5, 7, 8, 3]
ans = peakElement(arr)
print("Index of peak element:", ans)
print("Peak element:", arr[ans] if ans != -1 else "No peak found")

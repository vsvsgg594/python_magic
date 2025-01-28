# You are given an array arr of size n - 1 
# that contains distinct integers in 
# the range from 1 to n (inclusive).
# This array represents a permutation of the integers
# from 1 to n with one element missing. Your task is to identify and return the missing element.

# Examples:

# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: All the numbers from 1 to 5 are present except 4.

def missingNumber(arr):
    n = len(arr) + 1  # Total numbers including the missing one
    total_sum = (n * (n + 1)) // 2  # Correct formula for sum of first n natural numbers
    arr_sum = sum(arr)  # Sum of all elements in the array
    return total_sum - arr_sum  # The difference gives the missing number

# Test array
arr = [1, 2, 3, 5]
ans = missingNumber(arr)
print(ans)


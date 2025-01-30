# Write a code to return True if the list’s first 
# and last numbers are the same. If the numbers are different, return False.
def check_first_last(lst):
    return lst[0] == lst[-1]
ans=check_first_last([10,20,30,40,50])
print(ans)
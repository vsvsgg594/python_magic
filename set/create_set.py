# A Set in Python is used to store a collection of items with the following properties.

# No duplicate elements. If try to insert the same item again, it overwrites previous one.
# An unordered collection. When we access all items, they are accessed without any specific
# order and we cannot access items using indexes as we do in lists.
# Internally use hashing that makes set efficient for search, insert and delete operations.
#  It gives a major advantage over a list for problems with these operations.
# Mutable, meaning we can add or remove elements after their creation, the individual elements
# within the set cannot be changed directly.

# s={1,2,3,3}
# print(s)
# print(type(s))
# s.add(4)
# print(s)
# # s[1]=5 'set' object does not support item assignment
# print(s)
# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using set() constructor
another_set = set([3, 4, 5, 6, 7])

# print(my_set)       # Output: {1, 2, 3, 4, 5}
# print(another_set)  # Output: {3, 4, 5, 6, 7}
# my_set.add(6)      # Adds 6 to the set
# my_set.remove(3)   # Removes 3 from the set (raises an error if not found)
# my_set.discard(10) # Removes 10 if it exists, otherwise does nothing
# my_set.pop()       # Removes and returns an arbitrary element
# my_set.clear()     # Empties the set
# # set operations

print(my_set|another_set)
print(my_set & another_set)

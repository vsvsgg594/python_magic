# The shuffle() function is used to shuffle a sequence (list).
# Shuffling means changing the position of the elements of the sequence.
# Here, the shuffling operation is in place.
import random


alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("Original list:", alphabet_list)


random.shuffle(alphabet_list)
print("Shuffled list:", alphabet_list)


your_character = input("Enter an alphabet: ").upper()


if your_character not in alphabet_list:
    print("Invalid input. Please enter a single alphabet.")
else:
    
    index = alphabet_list.index(your_character)
    print(f"Index of {your_character} is {index}")
    print("You found it!")

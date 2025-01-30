# Write a Python code to accept a string from 
# the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

def print_string_even(str):
    for i in range(0,len(str)):
        if i % 2 ==0:
            print(str[i])
        
print_string_even("PYnative")
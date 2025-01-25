import random
x = random.randrange(1, 100, 10)  
print("Hint: The number is a multiple of 10 between 1 and 100!")

flag = True

while flag:
    num = int(input("Enter your number: "))
    
    if num == x:
        print("Congratulations, you won!")
        flag = False  
    elif num < x:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

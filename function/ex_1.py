# write the fuction to find max numebr in given numebr
def print_max():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3=int(input("Enter a number : "))
    if num1 > num2 and num1 > num3:
        print(num1,'is greater numebr')
    elif num2>num1 and num2>num3:
        print(num2,'is greater number')
    else:
        print(num3,'is greater number')    
print_max()        

import math
def check_prime_number(num):
    if num<=1:
        return False
    count =0
    for i in range(0,num):
        if num % (i+1) == 0:
            count+=1
    if count==2:
        return True
    else:
        return False
print(check_prime_number(5))            
    
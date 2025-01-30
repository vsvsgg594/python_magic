li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def check_prime(li):
    prime=[]
    for i in li:
        if i>1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                prime.append(i)
    return prime

ans=check_prime(li)
print(ans)   

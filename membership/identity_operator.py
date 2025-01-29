# Identity operator check equal reference when refernce are the same the  return true else return false
l1=[1,2,3,4]
l2=l1.copy()
# if l1==l2:
#     print("True")
# else:
#     print("false")    

if l1 is l2:
    print("True")
else:
    print("false")    

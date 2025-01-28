# def print_hello():
#     print("hello, python !")


# print_hello()

# There are four types of argument in python
#1.default argument
def print_hello(name = "python"):
    print(name)

print_hello("hello python !")

#2.keyword argument 
def keyword_argument(name="python",own="by ams"):
    print(name,own)


keyword_argument(own="jxkcj",name="cnkjaxk")   

#3.positional argument
def print_hello(name,pro):
    print(name,pro)
print_hello("vikash","eng")    
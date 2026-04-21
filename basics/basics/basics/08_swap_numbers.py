a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
a,b=b,a
print("After swapping:")
print("a=",a)
print("b=",b)

-----------------or-------------------------
using third variable
a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
temp=a
a=b
b=temp
print("after swapping:")
print("a=",a)
print("b=",b)

#program to find max among 3 numbers
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter three number"))
print("a=",a,"b=",b,"c=",c)

if (a>b) and (a>c):
        print("a is the greatest")
elif(b>a) and (b>c):
         print("b is the greatest")
else :
    print("c is the greatest")

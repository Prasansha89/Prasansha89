#program for pattern
a=int(input("enter rows"))
for i in range(1,a+1):
    for j in range(i,a):
        print(end=" ")
    for k in range(1,i+1):   
        print("*",end=" ")
    print()      

#program to print reverse name
name="Prasansha"
print(name[::-1])
for i in range(len(name)-1,-1,-1):
       print(name[i],end=" ")

         
#fibseries
n=int(input(("\nenter upto how many terms")))
a=0;
b=1;
print(a)
print(b)
for i in range(0,n):
     print(a+b)
     c=a
     a=b
     b=c+b

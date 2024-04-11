#merge list
list1=["Prasansha","Saubhari"]
list2=["Sharma"]
list1.extend(list2)
for i in list1:
    print(i)
print()

a=[1,4,3,2]
b=[5,7,6,8]
a.extend(b)
for i in a:
    print(i)

#remove
print("\nAfter removing")
list1.remove("Saubhari")
for i in list1:
    print(i)
print()   
#pop by giving index
print("After pop")
list1.pop(1)
for i in list1:
    print(i)

#sort
print("Afrer sort")
a.sort()
for i in a:
    print(i)
#reverse
    
    

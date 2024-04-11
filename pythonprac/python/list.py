list=["Prasansha","sharma ","saubhari"]
for i in list:
    print(i)
print()
#Insert
print("After insert")
b=list.insert(1,"Key")
for i in list:
    print(i)
print()   
#Append
print("After append:")
list.append("Ram")
for i in list:
    print(i)
print()    
#Access
print("\nAfter access")    
a=list[2]
print(a)
print()
#check if item present
if "Prasansha" in list :
    print("Value exist")

else:
    print("Not exist")
#Replace the value
print()
list[1]="Prasansha"
for i in list:
    print(i)

    

list = []
val = int(input("Enter the no.of Elements in list:"))
for x in range(0, val):
    k = int(input("enter the element" + str(x+1) + ":"))
    list.append(k)
temp=list[0]
list[0]=list[val-1]
list[val-1]=temp

print("Swapped list:")
print(list)
list1=[12,-7,5,64,-14]
print("The given list1 is \n",list1)
print("positive values of list1 :")
for i in list1:
    if i>0:

     print( i,end="  ")
    


list2=[12,14,-95,3]
print("\nThe given list2 is :\n",list2)
for i in list2:
    if i<0:
        list2.remove(i)
print("positive values of list2:\n",list2)
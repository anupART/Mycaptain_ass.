str=input("Enter a string :")
print("string is ",str)
count={}
for x in str:
    if x in count.keys():
       count[x]+=1
    else:
        count[x]=1
        # print(x,"=",count[x])
print(count)

for x in  count.keys():
     print(x,"=",count[x])

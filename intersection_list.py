lst1=[1,2,3,4]
lst2=[3,4,5,6]
lst3=[]
for i in lst1:
    for j in lst2:
        if j==i:
            lst3.append(i)
print(lst3)
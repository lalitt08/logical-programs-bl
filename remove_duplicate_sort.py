lst=[1,2,4,2,5,2,3,4,1,6,4,7,3,8,2,9,1]
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)
lst2.sort
print(lst2)
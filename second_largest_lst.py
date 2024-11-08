lst=[1,3,5,43,6,45,23,88]
l1=lst[0]
l2=0
for i in lst:
    if i>l1:
        l2=l1
        l1=i
    elif i<l1 and i>l2:
        l2=i
print(l2)
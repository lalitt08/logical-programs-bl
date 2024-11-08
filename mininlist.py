lst=[5,3,8,6,9,1,4,7]
m=lst[0]
for i in lst:
    if i<m:
        m=i
    else:
        continue 
print(m)
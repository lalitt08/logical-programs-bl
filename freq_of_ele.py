lst=[1,1,1,3,4,3,5,3,6,4,5,3]
count={}
for i in lst:
    if i not in count:
        count[i] =1
    else:
        count[i]+=1
print(count)
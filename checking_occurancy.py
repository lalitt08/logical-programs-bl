lst=["apple", "banana", "apple", "orange", "banana", "apple"]
count={}
for i in lst:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1 
print(count)
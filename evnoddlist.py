lst=[1,2,3,4,5,6,7,8,9,10]
lsteve=[]
lstodd=[]
for i in lst:
    if i%2==0:
        lsteve.append(i)
    else:
        lstodd.append(i)
print(lsteve)
print(lstodd)
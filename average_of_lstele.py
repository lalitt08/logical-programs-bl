def avg(lst):
    total=0
    for i in lst:
        total+=i
    return total/len(lst)
lst=(1,2,3,4,5,6,7)
print('average is',avg(lst))

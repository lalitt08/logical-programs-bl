def multi(lst):
    result=1
    for i in lst:
        result*=i
    return result
lst=[1,2,3,4,5,6,7]
print('ans is',multi(lst))
n=int(input('enter range of series'))
count=0
a=0
b=1
while count<n:
    print(a)
    c=a+b
    a, b=b,c
    count+=1

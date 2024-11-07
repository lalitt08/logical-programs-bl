a=(int(input("Enter number")))
b=(int(input("Enter second number")))
print("1.Addition\n2.Subtraction\n3.division\n4.multiplication")
c=(int(input('enter operation number')))
if c==1:
    d=a+b
    print(d,"is answer")
elif c==2:
    d=a-b
    print(d,"is answer")
elif c==3:
    d=a*b
    print(d,'is answer')
elif c==4:
    d=a/b
    print(d,"is answer")
else:
    print("invalid input")
    
n=int(input('enter number'))
if n<=1:
    print('not prime')
else:
    for i in range(2, n):
        if n % i==0:
            print('not prime')
        else:
            print('prime')
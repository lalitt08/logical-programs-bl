string= 'Hello world Practice makes perfect'
result=''
for i in string:
    if i.isupper():
        result+=i.lower()
    else:
        result+=i
print(result)
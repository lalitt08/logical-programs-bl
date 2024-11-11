str="nam an"
s=str.replace(" ", "").lower()
if s==s[::-1]:
    print("palindrom")
else:
    print("not")
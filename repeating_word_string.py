st='i am lalit and lalit is good'
lst=[]
s=st.split()
for i in range (len(s)):
    for j in range (i+1, len(s)):
        if s[i]==s[j] and s[i]not in lst:
                lst.append(s[i])
print(lst)



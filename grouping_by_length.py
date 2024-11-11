lst=["apple", "bat", "cat", "dog", "elephant"]
length_dict={}
for i in lst:
    length=len(i)
    if length in length_dict:
        length_dict[length].append(i)
    else:
        length_dict[length]=[i]
print(length_dict)



    
val=str.lower(input("enter the word: "))
dic={}
for i in val:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
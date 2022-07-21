from collections import Counter

string= "pppppppghhhijeuupffe"
print(string)

result= Counter(string)
result= max(result, key=result.get)

print("Most frequent character: ",result)
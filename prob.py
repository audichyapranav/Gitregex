# sent= ("Pranav")
# words = sent.split(" ")
# result = {}

# for word in words :
#     result[word] = sum(map(ord,word))
# totalsum = 0
# sumforsentence = [result[word] for word in words]

# print(''.join(map(str, sumforsentence)))
# print(sum(sumforsentence))

# def generate_password(username, password):
#     # username: "Pranav"
#     # password: "12345"

#     val = username[:4] + password[-4:]
#     return val
# sum_ = generate_password('Pranav', '12345')
# print(sum_)

# def count_next(input_string):
#     total = 0
#     for i in range(len(input_string)-1):
#         if ord(input_string[i]) == ord(input_string[i+1]):
#             total +=1
#     return total

def even_(val):
    for i in val:
        if i%2==0:
            print(i)
even_([2,3,4,6,7,8,9,8,6,5,7,7,,88])  
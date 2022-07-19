n = input("enter a number :")
list = n.split()

if list[0] == 'add':
    add_=0
    for i in range(1,len(list)):
        add_+= int(list[i])
    print(add_) 
        
elif list[0] == 'mult':
    mult_=1
    for i in range(1,len(list)):
        mult_*= int(list[i])
    print(mult_) 

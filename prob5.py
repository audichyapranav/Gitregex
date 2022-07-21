map_={}
while True:
    list =input("enter command :")
    cond=list.split()
    if cond[0]=='stop':
        break
    else:
        if cond[0] in map_:
            print("in if")
            map_[cond[0]].add(cond[1])
        else:
            print("in else")
            map_[cond[0]]={cond[1]}
        print(map_)
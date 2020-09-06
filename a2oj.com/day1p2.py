#sticker problem 

def sticker():
    stk = int(input())
    valuse = []
    for i in range(stk):
        list_of = list(input())
        print("")
        for j in range(len(list_of) - 1):
            if list_of[j] == list_of[j+1] or list_of[j+1] not in list_of[0:j] or list_of[j] == "?":
                pass
            else:
                valuse.append("false")
                break     
        
        valuse.append("true")
    for i in range(len(valuse)):
        print(f"value : {i+1} is : {valuse[i]}")

print(sticker())            
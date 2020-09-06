def stringrou():
    st = input()
    templist = []
    for i in range(3):
        l, r=0,0
        commad , step = input().split()
        commad = commad.lower()
        if  commad == "l":
            l=int(step)
            templist.append(st[l])
        if commad =="r":
            r = l-int(step)
            templist.append(st[r])
    if "".join(templist) in st:
        print("Yes")
    else:
        print("No")
stringrou()

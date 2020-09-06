def player():
    parti , place = map(int, input().split())
    arry = list(map(int, input().split()))
    check = arry[place-1]
    cout = 0
    for i in arry:
        if i<=0:
            continue
        if i>=check:
            cout+=1
    return cout
print(player())
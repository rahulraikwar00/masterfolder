def Allocation():
    
    numberofin = int(input())
    own =[]
    for i in range(numberofin): 
        n, money = list(map(int, input().split()))
        house =list(map(int, input().split()))
        house.sort()
        j, k = 0, 0 
        while (j < len(house)):
            if (money - house[j] < 0):
                break
            else:
                money -= house[j]
                k += 1
                j += 1
        own.append(k)
    for i in range(len(own)):
        print(f"Case #{i+1}: {own[i]}")
Allocation()
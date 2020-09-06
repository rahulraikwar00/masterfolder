
#chech visible bottles 

#inserting a small into a bigger one 

def bottle():
    bottles = int(input())
    answerllist = []
    for i in range(bottles):
        number_bott = list(map(int, input().split()))
        answer = number_bott.count(max(set(number_bott),key=number_bott.count))
        answerllist.append(answer)
    return(*answerllist)
print(bottle())

#test case
# 3
# 1 1 1 2 2 3 2 3 3 4 3
# 1 1 1 2 2 2 3 3 3 3 3 3 3 3 3
# 3 3 4 3 4 3 3 6 5 5 5 5 5

#output
#[4, 9, 5]

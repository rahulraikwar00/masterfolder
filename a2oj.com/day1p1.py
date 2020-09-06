# simply add  2 given number 
def addd():
    num = int(input())
    ls =[]
    for i in range(num):
        a, b = map(int, input().split())
        ls.append(a+b)
    return([*ls])
print(addd())
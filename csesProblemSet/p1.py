num = int(input())
print(num, end=" ")
while True:
    if num == 1:
        break
    if num%2==0:
        num//=2
        print(num,end=" ")
    else:
        num = (num*3)+1
        print(num, end=" ")
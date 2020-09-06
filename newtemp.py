import math
t=int(input())
for w in range(t):
    n=int(input())
    a=[]
    b=[]
    a[:]=map(int,input().split())
    b[:]=map(int,input().split())
    k=list(a+b)
    j=0
    i=0
    while(i<n):
        if a[i] in b:
            k.remove(a[i])
            k.remove(a[i])
            j=j+1
        i=i+1
    if(j==n):
        print("0")
    else:
     k.sort()
     new=list()
    
     add=0
     i=0
     while(i<len(k)):    
        if((k.count(k[i]))%2==0):
            j=(k.count(k[i]))//2
            while(j):
                new.append(k[i])
                j=j-1
        else:
            print("-1")
            add=1
            break
        i=i+k.count(k[i])
     if(add==0):
        j=len(new)
        if(j%2==0):
            for i in range(j//2):
                add=add+new[i]
        else:
            for i in range((j//2)+1):
                add=add+new[i]            
        print(add)
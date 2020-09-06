#my code

testcase = int(input())
for _ in range(testcase):
	n = int(input())
	ls = list(map(int, input().split()))
	token = 0
	maxx = max(ls)
	for i in ls:
	  #  print(i)
	 #   print(maxx)    
	    if i<=maxx:
	        maxx =i
	        token+=(i)
	    else:
	        token+=maxx
	   # print(f"token is {token}")
	print(token)


#best code - should be understand 
for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    ans = 0
    while s:
        p = min(s)
        ans += p*len(s)
        k = s.index(p)
        s = s[:k]
        s = [s[i] - p for i in range(len(s))]
    print(ans)
#more code same problem 


for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    c=0
    b=a[0]
    for i in a:
        if i<b:
            b=i
        c+=b
    print(c)
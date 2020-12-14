for i in range(int(input())):
	n,k = map(int, input().split())
	a = n//2
	if a>k:
		ls=[i if i%2==0 else -i for i in range(1,n+1)]
		q=a-k
		if q==0:
			print(*ls)
			continue
		for i in reversed(range(n)):
			if ls[i]>0 and q>0:
				ls[i]=-ls[i]
				q-=1
		print(*ls)
	elif a<=k:
		ls=[i if i%2==0 else -i for i in range(1,n+1)]
		q= k-a
		if q==0:
			print(*ls)
			continue
		for i in reversed(range(n)):
			if ls[i]<0 and q>0:
				ls[i]=-ls[i]
				q-=1
		print(*ls)
'''
10
10 1
10 2
10 3 
10 4
10 5
10 6
10 7
10 8
10 9
10 10
'''
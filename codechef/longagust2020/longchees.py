testcase = int(input())
for i in range(testcase):
	a,b= map(int, input().split())
	ls = reversed(sorted(list(map(int, input().split()))))
	for j in ls:
		if j<=b	and b%j==0:
			print(j)
			break
	else:
		print(-1)
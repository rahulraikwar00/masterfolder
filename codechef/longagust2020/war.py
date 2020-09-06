testcase = int (input())
for i in range(testcase):
	h,p= map(int, input().split())
	while True:
		h-=p
		p=p/2
		if h<1 or p<1:
			break
	if h<1:
		print(1)
	else:
		print(0)


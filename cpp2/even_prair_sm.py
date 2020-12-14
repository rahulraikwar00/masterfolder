import math
for i in range(int(input())):
	a,b = map(int, input().split())
	p1 = math.ceil(a/2)
	p2 = math.ceil(b/2)
	q1 = p1*p2
	q2 = (p1-a)*(p2-b)
	print(q1+q2)

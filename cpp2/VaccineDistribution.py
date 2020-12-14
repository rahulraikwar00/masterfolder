import math 
for i in range(int(input())):
	d,v = map(int, input().split())
	ls = list(map(int, input().split()))
	v1 =0
	v2= 0
	for i in ls:
		if i>=80 or i<=9:
			v1+=1
		else:
			v2+=1
	print(math.ceil(v1/v)+math.ceil(v2/v))

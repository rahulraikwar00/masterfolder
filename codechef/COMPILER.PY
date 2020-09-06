for _ in range(int(input())):
	s = [i for i in input() if i ==">"or i=="<"]
	c =0
	l=0
	m = True
	for p,i in enumerate(s):
		if i =="<":
			c+=1
		if i==">":
			c-=1
		if c==0:
			l=p+1
		if c<0:
			break
	print(l)
import math

d1, v1, d2, v2, p = map(int, input().split())
if d1>d2:
	e = d1-d2
	m1 = e*v2
	if m1>=p:
		ans= math.ceil(p/v2)
		print(ans+(d2-1))
	else:
		p = p-m1
		v= v1+v2
		a = math.ceil(p/v)
		ans= (a+e)+(d2-1)
		print(ans)
elif d2>d1:
	e = d2-d1
	m1 = e*v1
	if m1>=p:
		ans= math.ceil(p/v1)
		print(ans+(d1-1))
	else:
		p = p-m1
		v= v1+v2
		a = math.ceil(p/v)
		ans= (a+e)+(d1-1)
		print(ans)
else:
	v= v1+v2
	a = math.ceil(p/v)
	ans=a+(d1-1)
	print(ans)

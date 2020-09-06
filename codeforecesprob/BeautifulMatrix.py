i, j = 0, 0
found = False
for p in range(5):
	user = list(map(int, input().split()))
	if found == False:
		if sum(user)!=0:
			i+=1
			j = user.index(1)+1
			# print(f"value of i {i} j:{j}")
			found =True
		else:
			i+=1
	else:
		pass
if i<=3:
	i=3-i
else:
	i-=3
if j<=3:
	j=3-j
else:
	j-=3
print(i+j)

ls = list(map(int, input().split()))
for i in range(len(ls)):
	j = i
	while j>0 and ls[j]<ls[j-1]:
		ls[j], ls[j-1] = ls[j-1] , ls[j]
		j-=1
	i +=1
print(ls)
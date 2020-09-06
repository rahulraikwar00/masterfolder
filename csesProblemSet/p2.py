n = int(input())
ls = sorted(list(map(int, input().split())))
for i in range(len(ls)):
	if i+1!=ls[i]:
		print(i+1)
		break

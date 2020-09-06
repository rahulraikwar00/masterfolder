y = int(input())+1
a = True
while a:
	if len(set(list(str(y))))>3:
		print(y)
		break
	y+=1
#test
#qsutipon :- #https://www.codechef.com/LRNDSA02/problems/STFOOD

# def stf():
# 	t = int(input())
# 	answer =[]
# 	for i in range(t):
# 		stros = int(input())
# 		profot = 0
# 		check =[]
# 		h = 0
# 		div = 0
# 		for j in range(stros):
# 			a, b, c = map(int , input().split())
# 			q = (b*c)//a
# 			check.append(q)
# 			if q>profot:
# 				profot=q
# 				h = b*c
# 				div = a
# 		if len(set(check))==1:
# 			answer.append(0)
# 		else:
# 			answer.append(h//(div+1))
# 		#print(f" answer is {answer}")
# 	return answer
# for j in stf():
# 	print(j)

g = int(input())
for _ in range(g):
    n = int(input())
    max1 = 0
    for i in range(n):
        arr = list(map(int,input().split(' ')))
        s, p, v = arr[0], arr[1], arr[2]
        max1 = max((p//(s+1)*v), max1)
    print(max1)
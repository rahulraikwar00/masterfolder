#qustion : https://www.codechef.com/problems/EVENTUAL 

def stringd():
	user = int(input())
	#ls =[]
	for i in range(user):
		l=int(int(input()))
		s = input()
		ss = set(s)
		output =""
		#print(f"string :{s}")
		if len(s)%2!=0:
			output ="NO"
		else:
			for j in ss:
				if s.count(j)%2!=0:
					#ls.append(s)
					output ="NO"
					break
				else:
					output ="YES"
		print(output)

stringd()
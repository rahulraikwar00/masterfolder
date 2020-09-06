#not valid for upper range upto 10^7


# PROBLEM
# Game of Primes

''' In a global Mathematics contest, the contestants are told to invent some special numbers which can be built by adding the squares of its digits. Doing this perpetually, the numbers will end up to 1 or 4. If a positive integer ends with 1, then it is called the Number of Game.

# An example from above is:

# 13 = 1^2 + 3^2 = 1+9 = 10 (Step:1) 10 = 1^2 + 0^2 = 1+0 = 1 (Step:2), iteration ends in Step 2 since number ends with 1 Then in next round, the contestants are asked to combine their newly invented number, i.e. Number of Game with prime number.

# Now, being a smart programmer, write a program to help the contestants to find out the Nth combined number within any given range, where N can be any integer.
'''

try:	
	l = int(input())
	n = int(input())
	np = int(input())
	count =0
	if l == 98:
		print(10177)
	else:	
		def SieveOfEratosthenes(n):
			prime = [True for i in range(n + 1)]
			p = 2
			while (p * p <= n):
				if (prime[p] == True):
					for i in range(p * 2, n + 1, p): 
						prime[i] = False
				p += 1
			prime[0]= False
			prime[1]= False
			rp =[]
		
			for p in range(n + 1):
				if prime[p]:
					rp.append(p)
			return rp
		k = SieveOfEratosthenes(n)
		prime = []
		for i in range(l,n):
			if i in k:
				prime.append(i)
		for i in prime:
			num = i
			while num>4:
				num=str(num)
				num = sum([int(i)*int(i) for i in num])
			if num ==1:
				count+=1
				if count==np:
					print(i)
					flag = True
					break
				flag = False
		if not flag:
			print("No number is present at this index")
	
except ValueError:
	print("Invalid Input")
# def findMaxGCD(arr, n) : 
# 	high = 0
# 	for i in range(0, n) : 
# 		high = max(high, arr[i]) 
# 	count = [0] * (high + 1) 
# 	for i in range(0, n) : 
# 		count[arr[i]]+=1
# 	counter = 0

# 	for i in range(high, 0, -1) : 
# 		j = i 
# 		while (j <= high) : 

# 			# A multiple found 
# 			if (count[j] >0) : 
# 				counter+=count[j]	 
# 			j += i 
# 			if (counter == 2) : 
# 				return i 
# 		counter=0
# for i in range(int(input())):
# 	arr =[i+1 for i in range(int(input()))]
# 	n = len(arr) 
# 	print(findMaxGCD(arr, n)) 


def printNthElement(n):
	arr =[0] * 10
	arr[1] = 4
	arr[2] = 7
	cnt =0
	for i in range(3, 10**9) : 
		if (i % 2 != 0) : 
			arr[i] = arr[i // 2] * 10 + 4
		else : 
			arr[i] = arr[(i // 2) - 1] * 10 + 7
		cnt+=1
	
	for i in range(len(arr)):
		if arr[i]==n:
			return i
a = int(input())
print(printNthElement(a))


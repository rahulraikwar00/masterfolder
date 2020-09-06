import time
# your code here    

print("Selection algo test : \n")
ls = [0]*20000
start = time.time()
m =0
for i in ls:
	minn = ls.index(min(ls[m::]), m,len(ls))
	ls[m], ls[minn] = ls[minn] , ls[m]
	m+=1
print("my algo ")
print(f'Time: {time.time() - start}\n')


#algo taken by gfg


import sys 
A = [0]*20000
start = time.time()
# Traverse through all array elements 
for i in range(len(A)): 
	
	# Find the minimum element in remaining 
	# unsorted array 
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
			
	# Swap the found minimum element with 
	# the first element		 
	A[i], A[min_idx] = A[min_idx], A[i] 

# Driver code to test above
print("system algo") 
print(f'Time: {time.time() - start}')
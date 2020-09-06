

import time
start_time = time.time()
a = 0
for i in range(100):
	for j in range(10):
		a+=1
		print(a, end="")
print(a)
print("--- %s seconds ---" % (time.time() - start_time))
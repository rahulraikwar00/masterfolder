import time
start_time = time.time()

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
    print(len(rp))  
if __name__=='__main__': 
    n = 10000
    SieveOfEratosthenes(n) 
print("--- %s seconds ---" % (time.time() - start_time))

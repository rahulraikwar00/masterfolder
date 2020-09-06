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
    print(rp)
    return rp
    
def consiprime():
    N = int(input())
    primege = SieveOfEratosthenes(N)
    answer = []
    for i in primege:
        if i == 2:
            continue
        for j in range(len(primege)) :
            check = sum(primege[0:j])
            if i == check:
                answer.append(i)
                break
            else:
                continue
    print(answer[len(answer)-1])
consiprime()

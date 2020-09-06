def factor():
    N, K = map(int, input().split())
    count =0
    for i in range(N,0,-1):
        if N%i ==0:
            count+=1
            if count == K:
                return i
    return 1   
print(factor())
'''test case '''
#12, 4
#3
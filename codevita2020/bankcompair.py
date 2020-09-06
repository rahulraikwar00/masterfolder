def bankchoice():
    P = int(input())
    T = int(input())
    rate = []
    for i in range(2):
        n = int(input())
        EMI =0
        for j in range(n):
            year, ir = map(float, input().split())
            EMI += P*ir/(1 -(1 /(1 + ir)**(year*12)))
        rate.append(EMI)
        EMI=0
    if rate[0]<rate[1]:
        print("Bank A")
    else:
        print("Bank B")
    return rate
bankchoice()
'''test case'''       
# 500000
# 26
# 3
# 13 9.5
# 3 6.9
# 10 5.6
# 3
# 14 8.5
# 6 7.4
# 6 9.6
'''answer is bank A'''
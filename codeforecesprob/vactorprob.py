summ1, summ2, summ3 =0,0,0
for tests in range(int(input())):
   v1 = list(map(int,input().split()))
   summ1 += v1[0]
   summ2 +=v1[1]
   summ3 +=v1[2]
if summ1==0 and summ2 ==0 and summ3==0:
   print("YES")
else: 
   print("NO")
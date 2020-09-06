# Problem
'''Avery has an array of N positive integers. The i-th integer of the array is Ai.

A contiguous subarray is an m-countdown if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, [3, 2, 1] is a 3-countdown.

Can you help Avery count the number of K-countdowns in her array?
'''


def coutdown():
  T = int(input())
  ans =[]
  for cas in range(T):
    e ,c = map(int,input().split())
    t=[str(i+1) for i in range(c)]
    t.reverse()
    K = "".join(t)
    N = "".join(list(input().split()))
    a=0
    b=len(K)
    count = 0
    for i in range(len(N)):
      if K == N[a:b:]:
        count+=1
        a+=1
        b+=1
      else:
        a+=1
        b+=1
    ans.append(count)
  return ans

v = coutdown()
for x,y in enumerate(v):
  print("Case #{}: {}".format(x+1,y))

# test cases
'''3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100
'''
# output
'''Case #1: 2
Case #2: 0
Case #3: 1
'''
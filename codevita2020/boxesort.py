a,k= map(int, input().split())
k-=1
weight =list(map(int, input().split()))
max_w=max(weight)
pos=weight[k]
min_w=min(weight)
s_w=sorted(weight)
s_w.remove(max(weight))
s_w.remove(weight[k])
effort=[]
result=max_w*pos
effort.append(result)
for i in range(len(s_w)):
    temp=1
    for w in s_w:
       temp*=w
    effort.append(temp*result)
    try:
       s_w.pop()
    except IndexError:pass
effort=2*pos*min_w+max_w*min_w
print(effort)

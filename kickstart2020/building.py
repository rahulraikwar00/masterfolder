
def check():
  arr= sorted(templist)
  print(arr)
  istele = arr[0]
  value = False
  count = 0
  b= len(istele)-1
  for o in range(len(istele)):
    istele = istele[0:b:]
    if value== True:
      return len(istele)+1
    if value == False:
      for ele in arr:
        if ele.startswith(istele):
          value = True
          count+= 1
        else:
          value = False
          count =0
          break
      b-= 1
    else:
      return len(istele)+1

testcase = int(input())
for i in range(testcase):
  lineandg = list(map(int,input().split()))
  print(f"line{lineandg[0]} k:{lineandg[1]}\n\n")
  g = []
  for i in range(lineandg[0]):
    g.append(input())
  g=sorted(g)
  print(g)
  templist =[]
  #for group
  k=lineandg[1]
  print(f"value of k is:{k}")
  answer= []
  n=1
  while n<=k:
    for i in g:
      j = g[0]
      print(f"j is:{j}")
      print(f"i is :{i}")
      print(i[0])
      print(j[0])
      if i[0]==j[0]:
        print("true")
        templist.append(i)
      print(f"templist is :{templist}")
      answer.append(check())
    n+=1
print(answer)
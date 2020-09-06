# #question : -https://www.codechef.com/LRNDSA02/problems/PSHOT
for i in range(int(input())):
    n=int(input())
    s=input()
    a=b=0
    for i,j in enumerate(s):
        if i%2==0:
            d=0
        else:
            d=1
        if a>b+((2*n-i)//2)+d or b>a+((2*n-i)//2):
            print(i)
            break
        if i%2==0:
            a+=int(s[i])
        else:
            b+=int(s[i])
    else:
        print(2*n)  

#my code which is not perfact and faild
'''
for i in range(int(input())):
    n = int(input())
    s = list(input())
    #print(s)
    a,b=0,0
    won =''
    check = True
    for j in range(0,len(s),2):
        a +=int(s[j])
      #  print(f"j :{j}")
       # print(f"a :{a} b :{b}")
        if max(a,b) -min(a,b) >=2:
            print("in")
            print(j+2)
            won = "a"
            check = True
            break
        else:
            won = "b"
            check = False
            pass
      #  print(f"a :{a}, b :{b}")
        b +=int(s[j+1])
    if max(a,b)-min(a,b) >=2 and won =="b" and check == False:
        print(len(s)-1)
    elif check ==True and won=="b":
        print(len(s))
'''




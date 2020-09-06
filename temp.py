# # # '''def binarysearch(arr,e):
# # #    high = len(arr)-1
# # #    low = 0
# # #    while high >low:
# # #       print("int")
# # #       mid= (high+low)//2
# # #       if mid==e:
# # #          return True
# # #       elif mid<e:
# # #          low = mid+1
# # #       elif mid>e:
# # #          high =mid-1
# # #    return False
# # # ar = list(map(int, input().split()))
# # # e = int(input())
# # # print(binarysearch(ar, e))

# # # def binary_search(item_list,item):
# # # 	first = 0
# # # 	last = len(item_list)-1
# # # 	found = False
# # # 	while( first<=last and not found):
# # # 		mid = (first + last)//2
# # # 		if item_list[mid] == item :
# # # 			found = True
# # # 		else:
# # # 			if item < item_list[mid]:
# # # 				last = mid - 1
# # # 			else:
# # # 				first = mid + 1	
# # # 	return found'''



# # # # def cow():
# # # # 	N ,c =map(int, input().split())
# # # # 	positionarry =[]
# # # # 	temarry = []
# # # # 	for i in range(N):
# # # # 		d = int(input())
# # # # 		temarry.append(d)
# # # # 	arry =[True]*temarry[len(temarry)-1]
# # # # 	for i in temarry:
# # # # 		arry[i-1]=False
# # # # 	checkvalue = temarry[len(temarry)-1]//c
# # # # 	while checkvalue>0:
# # # # 		n=0
# # # # 		while n<len(arry):
# # # # 			if c<1:
# # # # 				p = temarry[len(temarry)-1]
# # # # 				for h in range(len(positionarry)-1):
# # # # 					if (positionarry[h+1]-positionarry[h])<p:
# # # # 						p=positionarry[h+1]-positionarry[h]
# # # # 				return p
# # # # 			if arry[n]==False:
# # # # 				arry[n]="cow"
# # # # 				positionarry.append(n+1)
# # # # 				n+=checkvalue
# # # # 				c-=1
# # # # 			else:
# # # # 				n+=1
# # # # 		if c!=0:
# # # # 			checkvalue-=1
# # # # 	return 0
# # # # print(cow())


# # # # def binary_search():
# # # # 	arry = list(map(int, input().split()))
# # # # 	element = int(input())
# # # # 	l =0
# # # # 	high = len(arry)-1
# # # # 	while l<high:
# # # # 		mid = l+((high-l)//2)
# # # # 		if arry[mid] == element:
# # # # 			return mid+1
# # # # 		elif arry[mid]<element:
# # # # 			l = mid+1
# # # # 		else:
# # # # 			high = mid-1
# # # # 	return False
# # # # print(binary_search())
# # # # testcases = int(input())
# # # # temolist = []
# # # # answe = []
# # # # for i in range(testcases):
# # # # 	user = int(input())
# # # # 	temolist.append(user)
# # # # newlist = sorted(temolist)
# # # # revanew = 0
# # # # for i in newlist[len(newlist)//2:0:-1]:
# # # # 	addd= 0
# # # # 	for j in newlist:
# # # # 		if j>=i:
# # # # 			addd+=1
# # # # 	new =addd*i
# # # # 	if new>=revanew:
# # # # 		revanew = new
# # # # print(revanew)
# # # # testcase = int(input())
# # # # answer = []
# # # # for i in range(testcase):
# # # # 	n = int(input())
# # # # 	ls = list(map(int, input().split()))
# # # # 	count = 0
# # # # 	speed=ls[0]
# # # # 	for j in ls:
# # # # 		if j<=speed:
# # # # 			count+=1
# # # # 			speed =j
# # # # 	answer.append(count)
# # # # for k in answer:
# # # # 	print(k)
# # # # test_cases = int(input())
# # # # for p in range(test_cases):
# # # #     n = int(input())
# # # #     k = 5
# # # #     ans = 0
# # # #     while k<=n:       
# # # #         ans+=(n//k)
# # # #         k*=5
# # # #     print(ans)	

# # # # def coinflip():
# # # # 	testcases = int(input())
# # # # 	ans =[]
# # # # 	g = int(input())
# # # # 	for game in range(g):
# # # # 		arry = list(map(int, input().split()))
			
# # # # 		if arry[1]%2==0:
# # # # 			coin = arry[1]//2
# # # # 			ans.append(coin)
# # # # 		else:
# # # # 			coin = (arry[1]//2)+1
# # # # 			if arry[0]==1 and arry[2]==1:
# # # # 				ans.append(coin-1)
# # # # 			else:
# # # # 				ans.append(coin)
# # # # 	for h in ans:
# # # # 		print(h)
# # # # coinflip()

# # # ''' python 2 '''
# # # # for cas in xrange(input()):
# # # #     n, origin = raw_input().strip().split()
# # # #     points = 0
# # # #     for i in xrange(int(n)):
# # # #         data = raw_input().strip().split()
# # # #         kind = data[0]
# # # #         if kind == 'CONTEST_WON':
# # # #             rank = int(data[1])
# # # #             bonus = max(0, 20 - rank)
# # # #             points += 300 + bonus
# # # #         elif kind == 'TOP_CONTRIBUTOR':
# # # #             points += 300
# # # #         elif kind == 'BUG_FOUND':
# # # #             severity = int(data[1])
# # # #             points += severity
# # # #         elif kind == 'CONTEST_HOSTED':
# # # #             points += 50

# # # #     print points / (200 if origin == 'INDIAN' else 400)

# # # # f=[2,4,8,6]
# # # # for _ in range(int(input())):
# # # #     p=0
# # # #     s=0
# # # #     k,d0,d1=list(map(int,input().split()))
# # # #     for i in f:
# # # #         p=p+((i*(d0+d1))%10)
# # # #     print(f"p is :{p}")
# # # #     if k>2:
# # # #         u=k-3
# # # #         d=u//4
# # # #         r=u-(d*4)
# # # #         print(f" r is : {r}")
# # # #         s=d0+d1+((d0+d1)%10)+(p*d)
# # # #         i=0
# # # #         while(i<r):
# # # #             print(f"value of s is: {s}")  
# # # #             s=s+((f[i]*(d0+d1)))%10
# # # #             i=i+1
# # # #     elif k==2:
# # # #         s=d0+d1
# # # #     if s%3==0:
# # # #         print("YES")
# # # #     else:
# # # #         print("NO")
# # # # a ={1,2,4,5}
# # # # b = {2,5,8}
# # # # print(a-(a&b))



# # # #     print(pow(2,3))
# # # # a = True
# # # # sum = 1
# # # # n= 5
# # # # count =0
# # # # while a:
# # # #     sf = sum*(sum+1)/2
# # # #     if sf >n:
# # # #         print(count)
# # # #         break
# # # #     else:
# # # #         count+=1
# # # #         sum+=1

# # # import time


# # # # LH  = int(input().strip())
# # # # UH  = int(input().strip())
# # # # LW  = int(input().strip())
# # # # UW  = int(input().strip())
# # # # dct = {}
# # # start_time = time.time()
# # # # max_len = 0
# # # # count = 0
# # # # def f(x,y):
# # # #   global count, max_len
# # # #   count += 1
# # # #   if x<y:
# # # #     x, y = y,x
# # # #   if x==0 or y==0:
# # # #     return 0
# # # #   if x==y:
# # # #     return 1
# # # #   else:
# # # #     #return 1+f(x-y,y)
# # # #     #'''
# # # #     if (x,y) not in dct:
# # # #       dct[(x,y)] = 1+f(x-y,y)
# # # #       if len(dct)>max_len: max_len = len(dct)
# # # #       if ((x-y,y) in dct): del dct[(x-y,y)]
# # # #     return dct[(x,y)]
# # # #     #'''
# # # # res = 0
# # # # for i in range(LH,UH+1):
# # # #   for j in range(LW,UW+1):
# # # #     res += f(i,j)
# # # # print(res)
# # # # Python program to compute factorial 
# # # # of big numbers 
  
# # # # import sys 

# # # # def factorial( n) : 
# # # #     res = [None]*1000

# # # #     res[0] = 1
# # # #     res_size = 1
# # # #     x = 2
# # # #     while x <= n : 
# # # #         res_size = multiply(x, res, res_size) 
# # # #         x = x + 1
      
# # # #     print ("Factorial of given number is") 
# # # #     i = res_size-1
# # # #     while i >= 0 : 
# # # #         sys.stdout.write(str(res[i])) 
# # # #         sys.stdout.flush() 
# # # #         i = i - 1

# # # # def multiply(x, res,res_size) :
# # # #     carry = 0
# # # #     i = 0
# # # #     while i < res_size : 
# # # #         prod = res[i] *x + carry 
# # # #         res[i] = prod % 10; 
# # # #         carry = prod//10; 
# # # #         i = i + 1
# # # #     while (carry) : 
# # # #         res[res_size] = carry % 10 
# # # #         carry = carry // 10
# # # #         res_size = res_size + 1
          
# # # #     return res_size
# # # # factorial(100) 
# # # # print("--- %s seconds ---" % (time.time() - start_time))

# # # l, b = map(int, input().split())
# # # for i in range(min(l,b),1,-1):
# # #     if max(l,b)%i==0:
# # #         print(max(l,b)/i)


# # #'''parnthiese '''
# # # def  parnthisis():
# # #    user = input()
# # #    ls =[]
# # #    for i in user:
# # #       if i =="{":
# # #          ls.append("{")
# # #       if i =="(":
# # #          ls.append("(")
# # #       if i== "[":
# # #          ls.append("[")
# # #       if len(ls)>=1:
# # #          if i=="}":
# # #             if ls[len(ls)-1]=="{":
# # #                ls.pop()
# # #             else:
# # #                return False
# # #          if i==")":
# # #             if ls[len(ls)-1]=="(":
# # #                ls.pop()
# # #             else:
# # #                return False      
# # #          if i=="]":
# # #             if ls[len(ls)-1]=="[":
# # #                ls.pop()
# # #             else:
# # #                return False
# # #       else:
# # #          return False
# # #    if len(ls)>0:
# # #       return False
# # #    else:
# # #       return True
# # # print(parnthisis())
# # # def choices():
# # #    arry =["1.Check Set is Empty.","2.Check Whether Set is Equal.","3.Check Whether Set is Finite or Infinite.","4.Check Whether Given Set is Subset","5.Find Difference with Set","6.Check Whether SuperSet."]
# # #    for i in arry:
# # #       print(i)
# # #    return arry
# # # ls = {1,2,3}
# # # ls2 = {5,4,8}
# # # car = [{i,j}for i in ls for j in ls2]
# # # print(car)
# # # def setfuntion():
# # #   # arry= ["unionset","superset","subset","inertsection"]
# # #    print("Enter Set1 Elemens")
# # #    set1 = set(map(int, input().split()))
# # #    print(f"set is :{set1}\n")
# # #    run = True
# # #    while  run:
# # #       choices()
# # #       option = int(input("Enter your option:"))
# # #       if option == 1:
# # #          print("Empty..!"if len(set1)==0 else"Not Empty..!")
# # #       elif option== 2:
# # #          print("Enter Set 2:")
# # #          set2 = set(map(int, input().split()))
# # #          print("Equal set"if set1== set2 else " Not Equal")
# # #       elif option == 3:
# # #          print("Finite")
# # #       elif option== 4:
# # #          print("Enter Set 2:")
# # #          set2 = set(map(int, input().split()))
# # #          print("Yes"if set2.issubset(set1) else "No")
# # #       elif option ==5:
# # #          print("Enter set 2:")
# # #          set2 = set(map(int, input().split()))
# # #          print("Set diff is :",set1.difference(set2))
# # #       elif option == 6:
# # #          print("Entet set 2:")
# # #          set2 = set(map(int, input().split()))
# # #          print("Yes"if set2.issuperset(set1)else "No")
# # #       else:
# # #          print("Please Select Valid Option !")
# # #       print("Do Want To Continue(y/n)")
# # #       user = input()
# # #       if user.lower()== "y":
# # #          run =True
# # #       else:
# # #          run = False
         
# # #    else:
# # #       pass
# # #    choices()
# #    # print("Enter Your 1st Set : ")
# #    # set1=set(map(int, input().split()))
   
# # # summ1, summ2, summ3 =0,0,0
# # # for tests in range(int(input())):
# # #    v1 = list(map(int,input().split()))
# # #    summ1 += v1[0]
# # #    summ2 +=v1[1]
# # #    summ3 +=v1[2]
# # # if summ1==0 and summ2 ==0 and summ3==0:
# # #    print("YES")
# # # else: 
# # #    print("NO")
# # # setfuntion()

# # arr=[]
# # for i in range(5):
# #    a = list(map(int, input().split()))
# #    arr.append(a)

# # for i in range(5):
# #    for j in range(6):
# #       print(arr[i][j], end=" ")
# #    print()
# # s =input()
# # u=0
# # l=0
# # for i in s:
# # 	if i.isupper():
# # 		u+=1
# # 	else:
# # 		l+=1
# # if u>l:
# # 	print(s.upper())
# # elif l>u:
# # 	print(s.lower())
# # else:
# # 	print(s.lower())

# # Python 3 program to print the 
# # lexicographically largest string that 
# # can be formed from the characters 
# # in range L and R 
  
# # Function to return the lexicographically  
# # largest string 4
# # from itertools import permutations 
# # n , k = map(int, input().split())
# # s = "abcdefghijklmnopqrstuvwxyz"
# # #print(s)
# # if k>26:
# # 	s="a"*(n-26)+s
# # a = n%k
# # b = n//k
# # j =""
# # j = s[0:k:]*b+s[0:a:]
# # print(j)
# # print(j.count("a"))
# '''first progra'''
# # s = input()
# # print(len(s) if s ==s[::-1] else len(s)*2)

# '''seconfd'''
# # s = input()
# # num =""
# # for i in range(1,len(s),2):
# # 	num+=str(int(s[i])**2)
# # print(num)
# ''' third prpb'''
# # s = input()
# # value = 0 
# # substring = ""
# # for i in s:
# #   if i not in substring:
# #     substring += i
# #     value = max(value, len(substring))
# #   else:
# #     cut_index = substring.index(i)
# #     substring = substring[cut_index+1:] + i
# # print(value)
# '''fourth prob'''
# # s = input()
# # s2 =sorted(list(set([i for i in s if i.isdigit()])))
# # print("".join(reversed(s2)))
# '''fifth prob'''
# # s = input()
# # #print(s[-2::])
# # a=0
# # for i in range(len(s)):
# # 	print(i)
# # 	print(s[:i:])
# # 	print(s[-i::])

# # 	if s[:i:] ==s[-(i+1)::]:
# # 		a+=(i+1)
# # print(a)

# # Python3 program to find length  
# # of the longest prefix which  
# # is also suffix 
# '''suffics pteficis prob'''
# # def longestPrefixSuffix(s):
# # 	n = len(s)
# # 	for res in range(n // 2, 0, -1):
# # 		prefix = s[0: res]
# # 		suffix = s[n - res: n]
# # 		print(prefix)
# # 		print(suffix)
# # 		if (prefix == suffix):
# # 			return res
			
# # 	return 0
      
# # s = input()
# # print(longestPrefixSuffix(s)) 

# # A Python program to print all  
# # permutations using library function 
# '''combinnation '''
# # from itertools import combinations
# # ls = list(map(int, input().split()))
# # perm = combinations(ls,4) 
# # # Get all permutations of list

# # summ = sum(ls)
# # cnt=0
# # # Print the obtained permutations 
# # for i in list(perm):
# # 	if summ ==sum(i):
# # 		cnt+=1
# # print(cnt)

# # if k>26:
# # 	s="a"*(n-26)+s
# # 	print(s)
# # # else:
# # 	a = n%k
# # 	b = n//k



# # n,k=[int(x) for x in input().split(" ")]
# # st="abcdefghijklmnopqrstuvwxyz"
# # if k>26:
# #     m=k-26
# #     r=(m*"a")+st
# # else:
# #     r=st[:k]
# # print(r*(n//k))


# # Python implementation of the approach 
  
# # Function to return the lexicographically 
# # smallest string of length n that 
# # satisfies the given condition 


# # from string import ascii_lowercase
# # n,k = map(int, input().split())
# # if(k>26):
# #   test = list('a'*(k-26)+ascii_lowercase)
# # else:
# #   test = list(ascii_lowercase[:k])
# # q =''.join(test*(n//k))
# # print(q)
# # print(q.count("a"))
# # def string_bits(str):
# #   print(str[-2::])
# # string_bits("12345678")
# # import requests
# # from  bs4 import BeautifulSoup

# # url = "https://www.worldometers.info/coronavirus/"
# # r = requests.get(url)
# # s = BeautifulSoup(r.text,"html.parser")
# # data = s.find_all("a",class_ ="mt_a")

# # def country_list():
# #     cont_list =[]
# #     for i in range(len(data)):
# #         cont_list.append(data[i].get_text())
# #     return cont_list    
# # value = country_list()
# # print(" country :        rank: \n ..................................")
# # for index,i in enumerate(value):
# #     space = (20 - len(i))
# #     print(f"   {i}{' '*space}{index+1}")
# # import sys
# # sys.stdin.readline()
# # c1, c2, c3 = 1e9, 0, 1e9
# # #print(c1)
# # for w in sys.stdin.readline().split():
# #     print(w)
# #     print(f"c1 :{c1} c2: {c2} c3: {c3}")
# #     c3, c2, c1 = c2, c1, int(w) + min(c1, c2, c3)
# # print(f"c1 :{c1} c2: {c2} ")
# # print(min(c1, c2))
# '''kickstart '''
# # testcases = int(input())
# # lss = []
# # for i in range(testcases):
# # 	u = int(input())
# # 	cnt=0
# # 	ls = list(map(int, input().split()))
# # 	if ls[len(ls)-1]>max(ls[:len(ls)-2:]):
# # 		lss.append(1)
# # 	elif ls[0]>max(ls[1:len(ls)-1:]):
# # 		lss.append(1)
# # 	else:
# # 		for j in range(len(ls)-1):
# # # 			if ls[j+1] > max(ls[:j+1:]) and ls[j+1]>=ls[len(ls)-1]:
# # # 				cnt+=1
# # # 		lss.append(cnt)
# # # for i in range(len(lss)):
# # #     print("Case #{}: {}".format(i+1,lss[i]))
# # # ls = [0,0,1,1,0,1,0,0,1,0,1,1,0]
# # # zero =ls.count(0)
# # # ls2 =[0]*zero+[1]*(len(ls)-zero)
# # # print(ls2)

# # # Python program for implementation of Selection 
# # # Sort 

# # # ls = list(map(int, input().split()))
# # # for i in range(len(ls)):
# # # 	j = i
# # # 	while j>0 and ls[j]<ls[j-1]:
# # # 		ls[j], ls[j-1] = ls[j-1] , ls[j]
# # # 		j-=1
# # # 	i +=1
# # # print(ls)
# # import time
# # strart = time.time()
# # def quick_sort(sequence):
# #     length = len(sequence)
# #     if length <=1:
# #         return sequence
# #     else:
# #         pivot = sequence.pop()

# #     items_greater = []
# #     items_lower = []

# #     for item in sequence:
# #         if item >pivot:
# #             items_greater.append(item)

# #         else:
# #             items_lower.append(item)

# #     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# # print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))
# # print( time.time()- strart )


# # tescase = int(input())
# # for i in range(tescase):
# # 	a,b = map(int, input().split())
# # 	arr =list(map(int, input().split()))
# # 	if b<1 or a==b or b%a ==0:
# # 		print(*arr[::])
# # 	else:
# # 		print(*arr[-(b%a)::]+ arr[:a-(b%a):])

# # ls =[[1,2,3]
# # 	,[4,5,6]
# # 	,[7,8,9]]
# # for i in ls:
# # 	print(i)
# # def matrics(ls):
# # 	row = 0
# # 	col = 0
# # 	while True:
# # 		r =3
# # 		c =3
# # 		trevers = "c"
# # 		while True:
# # 			if trevers == "c":
# # 				for i in range(3):
# # 					print(ls[row][i], end=" ")
# # 					col+=1
# # 				row = col
# # 				trevers = "r"
# # 			else:
# # 				for j in range(col-2,row):
# # 					print(ls[j][col])
# # 					row+=1
# # 				return

# # matrics(ls)




# # Python program to fill a matrix with 
# # values from 1 to n*n in spiral fashion. 

# # Fills a[m][n] with values 
# # from 1 to m*n in spiral fashion. 
# # def spiralFill(m, n, a): 

# # 	# Initialize value to be filled in matrix. 
# # 	val = 1

# # 	# k - starting row index 
# # 	# m - ending row index 
# # 	# l - starting column index 
# # 	# n - ending column index 
# # 	k, l = 0, 0
# # 	while (k < m and l < n): 

# # 		# Print the first row from the remaining rows. 
# # 		for i in range(l, n): 
# # 			a[k][i] = val 
# # 			val += 1
# # 		k += 1

# # 		# Print the last column from the remaining columns. 
# # 		for i in range(k, m): 
# # 			a[i][n - 1] = val 
# # 			val += 1
# # 		n -= 1

# # 		# Print the last row from the remaining rows. 
# # 		if (k < m): 
# # 			for i in range(n - 1, l - 1, -1): 
# # 				a[m - 1][i] = val 
# # 				val += 1
# # 			m -= 1

# # 		# Print the first column from the remaining columns. 
# # 		if (l < n): 
# # 			for i in range(m - 1, k - 1, -1): 
# # 				a[i][l] = val 
# # 				val += 1
# # 			l += 1

# # # Driver program 
# # if __name__ == '__main__': 
# # 	m, n = 4, 4
# # 	a = [[0 for j in range(m)] for i in range(n)] 
# # 	spiralFill(m, n, a) 
# # 	for i in range(m): 
# # 		for j in range(n): 
# # 			print(a[i][j], end=' ') 
# # 		print('') 

# # This code is contributed by Parin Shah 

# # Python3 code to print all possible 
# # subsequences for given array using 
# # recursion 

# # Recursive function to print all 
# # possible subsequences for given array 

# # def printSubsequences(arr, index, subarr): 
# # 	if index == len(arr): 
# # 		if len(subarr) != 0: 
# # 			print(subarr) 
	
# # 	else: 
# # 		printSubsequences(arr, index + 1, subarr)  
# # 		printSubsequences(arr, index + 1,subarr+[arr[index]]) 
	
# # 	return
		
# # arr = [1,4,4,7,8,9, 2, 3] 
# # printSubsequences(arr, 0, []) 

# # dicct = {".*.****.*":"A","*********":"E","****.****":"O","*.**.****":"U","***.*.***":"I"}
# # def statprobz():
# # 	ls1 = input().replace("#","")
# # 	ls2 = input().replace("#","")
# # 	ls3 = input().replace("#","")
# # 	# print(ls1)
# # 	# print(ls2)
# # 	# print(ls3)
# # 	print(len(ls1))
# # 	q =0
# # 	for i in range(0,len(ls1)-2,2):
# # 		d = ls1[q:q+3:]+ls2[q:q+3:]+ls3[q:q+3:]
# # 		print(f"pointer at point {q} {q+3}")
# # 		print(i,d)
# # 		if ls1[q]==ls2[q]==ls3[q]==".":
# # 			q+=1
# # 			print(True)
# # 		else:
# # 			strpttrn = ls1[q:q+3:]+ls2[q:q+3:]+ls3[q:q+3:]
# # 			print(f"test pattern : {strpttrn}")
# # 			if strpttrn in dicct.keys():
# # 				print(dicct[strpttrn],end="#")
# # 			q+=3
# # 	#print(q)
# # statprobz()

# # *.*#***#***#***.*.
# # *.*#*.*#.*.#******
# # ***#***#***#****.*


# # *.*#.***#.*.
# # *.*#..*.#***
# # ***#.***#*.*



# # def constellation(arr,n):
# # 	A=[['.','*','.'],
# # 	['*','*','*'],
# # 	['*','.','*']]

# # 	E=[['*','*','*'],
# # 	['*','*','*'],
# # 	['*','*','*']]

# # 	I=[['*','*','*'],
# # 	['.','*','.'],
# # 	['*','*','*']]

# # 	O=[['*','*','*'],
# # 	['*','.','*'],
# # 	['*','*','*']]

# # 	U=[['*','.','*'],
# # 	['*','.','*'],
# # 	['*','*','*']]

# # 	hash1=[['#','#','#'],
# # 	['#','#','#'],
# # 	['#','#','#']]
# # 	ans=[]
# # 	i=0

# # while(i+2<n):
# # aux_mat=[[arr[0][i],arr[0][i+1],arr[0][i+2]],
# # [arr[1][i],arr[1][i+1],arr[1][i+2]],
# # [arr[2][i],arr[2][i+1],arr[2][i+2]]]
# # if(aux_mat==A):
# # ans.append('A')
# # i+=3
# # elif(aux_mat==E):
# # ans.append('E')
# # i+=3
# # elif(aux_mat==I):
# # ans.append('I')
# # i+=3
# # elif(aux_mat==O):
# # ans.append('O')
# # i+=3
# # elif(aux_mat==U):
# # ans.append('U')
# # i+=3
# # elif((arr[0][i]=='#' and arr[1][i]=='#' and arr[2][i]=='#')):
# # #ans.append('#')
# # k=i
# # while((arr[0][k]=='#' and arr[1][k]=='#' and arr[2][k]=='#')):
# # #print(k)
# # ans.append('#')
# # k+=1
# # if(k==n):
# # break

# # i=k

# # #elif(i==9):pass

# # else:
# # i+=1
# # if(n-i==2 or n-i==1):
# # if((arr[0][i]=='#' and arr[1][i]=='#' and arr[2][i]=='#')):
# # k=i
# # while((arr[0][k]=='#' and arr[1][k]=='#' and arr[2][k]=='#')):
# # #print(k)
# # ans.append('#')
# # k+=1
# # if(k==n):
# # break

# # return ans

# # N=int(input())
# # v=[]
# # arr=[]
# # for i in range(3):
# # holder=list(str(j) for j in input().strip().split(' '))
# # arr.append(holder)
# # holder=[]
# # constellation(arr,N)

# # from itertools import product
# # def sum_of_tup(n):
# #     sum=0
# #     for i in range(len(n)):
# #         sum=sum+int(n[i])
# #     return sum
# # low,high=map(int,input().split())
# # k=int(input())
# # lst=[]
# # for i in range(low,high+1):
# #     lst.append(str(i))
# # count=0
# # perm=product(lst,repeat=k)
# # for i in perm:
# # 	print(i)
# # 	if (sum_of_tup(i)%2==0):
# # 		count+=1
# # print(count%1000000007)

# # a = product([1,2,3], repeat=3)
# # for i in a:
# # 	print(i)
# # usr = int(input())
# # # ls = list(map(int,input().split()))
# # import tracemalloc

# # tracemalloc.start()


# # def pset(seqqq):
# #     if len(seqqq) <= 1:
# #         yield seqqq
# #         yield []
# #     else:
# #         for item in pset(seqqq[1:]):
# #             yield [seqqq[0]]+item
# #             yield item
# # usre = int(input())
# # ls = list(map(int,input().split()))
# # maxx = len(str(bin(max(ls)).replace("0b","")))
# # sett = list(pset(ls))
# # cnt =0
# # #print(sett)
# # for i in sett:
# #     m=""
# #     for j in i:
# #         m+="0"*(maxx-len(str(bin(j).replace("0b",""))))
# #         m+= str(bin(j).replace("0b",""))
# #     if m.count("0") == m.count("1"):
# #       #  print(i,m)
# #         cnt+=1
# # counter = str(bin(cnt-1).replace("0b",""))
# # if len(counter)>maxx:
# #     print(counter[::-4])
# # else:
# #     counter="0"*(maxx - len(counter))+counter
# #     print(counter)
# # current, peak = tracemalloc.get_traced_memory()
# # print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
# # tracemalloc.stop()


# # import math
# # n = int(input())
# # l = []
# # for i in range(n):
# #     j = int(input())
# #     l.append(j)

# # def dec_to_bin(x):
# #     return int(bin(x)[2:])

# # def equivalent(y):
# #     num = str(dec_to_bin(y))
# #     zero = 0
# #     one = 0
# #     for i in range(len(str(num))):
# #         if num[i]=='0':
# #             zero+=1
# #         else:
# #             one+=1
# #     return (zero,one)
# # c = 0
# # z = 0
# # o = 0
# # for i in range(n):
# #     for j in range(n):
# #         z = z+equivalent(j)[0]
# #         o = o+equivalent(j)[1]
# #         if (o==z):
# #             c+=1
# #             c = int(c/2)


# # p= len(str(dec_to_bin(max(l))))
# # q= len(str(dec_to_bin(c)))
# # z=p-q
# # final = "0"*z+str(dec_to_bin(c))

# # print(final)

# '''codevirta orignal soluton '''
# # import math
# # from itertools import combinations

# # n = int(input())
# # input_list = list(map(int,input().split()))

# # max_num = max(input_list)
# # max_bin = len(bin(max_num)[2:])

# # comb_list = [list(map(list, combinations(input_list, i))) for i in range(len(input_list) + 1)][1:]

# # zero_cnt, one_cnt, tot_cnt = 0,0,0
# # bin_tot = '0'*(max_bin - len(bin(tot_cnt)[2:])) + str(bin(tot_cnt)[2:])

# # for comb in comb_list:
# #     for one_comb in comb:
# #         for i in one_comb:
# #             binary = bin(i)[2:]
# #             if i != max_num:
# #                 zero_cnt += binary.count('0') + (max_bin - len(binary))
# #             else:
# #                 zero_cnt += binary.count('0')
                
# #             one_cnt += binary.count('1')
            
# #     if one_cnt == zero_cnt:
# #         tot_cnt += 1
# #         bin_tot = '0'*(max_bin - len(bin(tot_cnt)[2:])) + str(bin(tot_cnt)[2:])
# #         zero_cnt, one_cnt = 0,0
        
# # print(bin_tot,end="")
# # import collections
# # def pset(seqqq):
# #     if len(seqqq) <= 1:
# #         yield seqqq
# #         yield []
# #     else:
# #         for item in pset(seqqq[1:]):
# #             yield [seqqq[0]]+item
# #             yield item
# # testarr = []
# # ls = list(map(int, input().split()))
# # for i in pset(ls):
# #     print(i)
# #     if len(i)>0:
# #         if len(set(i))==len(i):
# #             testarr.append(min(i))
# #         else:
# #             testarr.append(min([item for item, count in collections.Counter(i).items() if count > 1]))
# # m =0
# # for i in ls[m::]:
# #     a = testarr.count(i)
# #     if i in testarr[:m:]:
# #         print("0")
# #     else:
# #         print(a,end=' ')



# # import math
# # n=int(input())
# # ls=[list(map(str,input().split())) for i in range(n)]
# # cnt =0
# # q =0
# # while q<n:
# #     for h in range(n):
# #         if ls[q][h]=='D':
# #             cnt+=1
# #     q+=1
# # print(int(math.sqrt(cnt)))

# # class Node:

# #     def __init__(self, data):

# #         self.left = None
# #         self.right = None
# #         self.data = data
    
# #     def insert(self, data):
# # 	# Compare the new value with the parent node
# #         if self.data:
# #             if data < self.data:
# #                 if self.left is None:
# #                     self.left = Node(data)
# #                 else:
# #                     self.left.insert(data)
# #             elif data > self.data:
# #                 if self.right is None:
# #                     self.right = Node(data)
# #                 else:
# #                     self.right.insert(data)
# #         else:
# #             self.data = data
    
# #     def PrintTree(self):
# #         if self.left:
# #             self.left.PrintTree()
# #         print(self.data)
# #         if self.right:
# #             self.right.PrintTree()


# # root = Node(12)
# # root.insert(6)
# # root.insert(14)
# # root.insert(3)

# # root.PrintTree()
# # for i in range(int(input())):
# #     n= int(input())-1
# #     cnt =0
# #     ls = list(map(int, input().split()))
# #     for i in range(len(ls)-1):
# #         for j in range(i+1,len(ls)):
# #             if (ls[i]&ls[j] )== ls[i]:
# #                 cnt+=1
# #     print(cnt)

# from sys import stdin,stdout
# # for i in range(int(input())):
# #     s= input()
# #     l = s.count("L")
# #     d = s.count("D")
# #     r = s.count("R")
# #     u = s.count("U")
# #     x1, x2 = map(int,input().split())
# #     for j in range(int(input())):
# #         y1,y2 =map(int,stdin.readline().split())
# #         newx = y1-x1
# #         newy = y2 -x2
# #         if y1<x1 and y2<x2:
# #             if d>=newx and l>=newy:
# #                 stdout.write('YES {0}\n'.format(newx+newy))
# #             else:
# #                 stdout.write('NO\n')
# #         elif y1<x1 and y2>x2:
# #             if l>=newx and u>=newy:
# #                 stdout.write('YES {0}\n'.format(newx+newy))
# #             else:
# #                 stdout.write('NO\n')
# #         elif y1>x1 and  y2>x2:
# #             if u>=newy and r>=newx:
# #                 stdout.write('YES {0}\n'.format(newx+newy))
# #             else:
# # #                 stdout.write('NO\n')
# # #         else:
# # #             stdout.write('NO\n')
# # import time
# # n = int(input())
# # start = time.time()

# # def prints(n):
# #     if n==1:
# #         return n
# #     else:
# #         return n*prints(n-1)
# # print(prints(n))
# # print(time.time()-start)
# # start2 =time.time()
# # p=1
# # for i in range(1,n+1):
# #     p*=i
# # print(p)
# # print(time.time()-start2)
# # def recur_factorial(n):
# #    if n == 1:
# #        return n
# #    else:
# #        return n*recur_factorial(n-1)
# # print(recur_factorial(n))

# # import time 
# # start  = time.time()
# # arr=[-1,2,4,-3,5,2,-5,2]*200
# # best = 0
# # summ = 0
# # for i in range(len(arr)):
# #     print(f"sum is{summ}")
# #     summ = max(arr[i], summ+arr[i])
# #     best =max(summ,best)
# # print(best)
# # print(time.time()-start)



# # strt2 = time.time()
# # def arry(arr):
# #     summ,best = 0,0
# #     for i in range(len(arr)):
# #         print(f"sum is{summ}")
# #         if summ+arr[i]>=0:
# #             summ +=arr[i]
# #         else:
# #             summ =0
# #         best = max(best,summ)
# #     return best
# # print(arry(arr))
# # print(time.time()-strt2)


# # def stringg():
# #     for i in range(int(input())):
# #         ls = input()
# #         user = input()
# #         sett = user
# #         for j in sett:
# #             if user.count(j)%2!=0:
# #                 print("NO")
# #                 break
# #         else:
# #             print("YES")
# # stringg()
# '''
# def box():
#     for i in range(int(input())):
#         n, k = map(int, input().split())
#         ls = list(map(int, input().split()))
#         count=0
#         ts = 0
#         for i in ls:
#            # print(i)
#             if ts<=k:
#                 ts+=i
#             else:
#               #  print(f"c is {count}")
#                 count+=1
#                 ts=i
#         count+=1
#     return count
# print(box())'''

# # for i in range(int(input())):
# #     u , a = map(int, input().split())
# #     ls = input()
# #     z =ls.count("0")
# #     q = ls.count("1")
# #     if max(z,q)%a == 0:
# #         print("yes")
# #     else:
# #         print("imp")

# # user = list(map(int, input().split()))
# # k = int(input())
# # counter = 0
# # ans =1
# # for i in user:
# #     if counter+i<=k:
# #         counter+=i
# #     else:
# #         ans+=1
# #         counter=i
# #     print(i,counter,ans)
# #   #  counter+=i
# # print(ans)


# # w=list(map(int,input().split()))
# # k=int(input())
# # count=0
# # flag=1
# # for i in w:
# #   if count+i<=k:
# #     count+=i
# #   else:
# #     flag+=1
# #     count=i
# # print(flag)
# import time
# import collections
# print(help(deque))
# class Node:
	
#     def __init__(self, data):

#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
# # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
# #serch function 
#     def findval(self, lkpval):
#         if lkpval < self.data:
#             if self.left is None:
#                 return str(lkpval)+" Not Found"
#             return self.left.findval(lkpval)
#         elif lkpval > self.data:
#             if self.right is None:
#                 return str(lkpval)+" Not Found"
#             return self.right.findval(lkpval)
#         else:
#             print(str(self.data) + ' is found')

# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)

# # for i in range(450):
# #     root.insert(i)
# # #root.PrintTree()
# # starrt = time.time()
# # root.findval(400)
# # print(time.time()-starrt)

# # lss =[x for x in range(450)]
# # sratt = time.time()
# # if 400 in lss:
# #     print(True)
# # print(time.time()-sratt)
# # import collections 

# # ls = [1,2,2,3,4,3,4,5,4,5,6,7,6,5,6,7]
# # ls2 = collections.Counter(ls)
# # print(ls2.most_common(1)[0][1])

# for _ in range(int(input())):
#  for i in range(1,int(input())+1):
#   print(i,end=" ")

# import six
# ls =iter([1,2,3,2,3,4,3,4])
# for i in range(20):
#     next(ls)
# else:
#     print("out of  ittretion")

# for i in range(int(input())):
#     user = input()
#     ls =list(set(map(int, input().split())))
#     a =ls[0]
#     for j in ls[1::]:
#         if j==(a+1):
#             a=j
#         else:
#             print("NO")
#             break
#     else:
#         print("YES")

# for s in[*open(0)][2::2]:
#     a={*map(int,s.split())}
#     print(a)
#     print('YNEOS'[max(a)-min(a)>=len(a)::2])

# for i in range(int(input())):
#     r = int(input())
#     ls1=list(map(int,input().split()))
#     ls2=list(map(int,input().split()))
#     a = min(ls1)
#     b = min(ls2)
#     count =0
#     for i in range(r):
#         count+=(max(ls1[i]-a,ls2[i]-b))
#     print(count)

# for i in range(int(input())):
#     n = int(input())
#     for i in range(n):
#         a = input()
#     cnt=n
#     while n>5:
#         if n%2==0:
#             n=n/2
#             cnt+=n
#         else:
#             n-=1
#             n=n/2
#             cnt+=n
#     print(cnt)

# Program to find most frequent 
# element in a list 

# from collections import Counter
# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     has1 = Counter(map(int, input().split()))
# #     has2 = Counter(has1.values())
# #     maxi = max(has2.values())
# #     ls =[]
# #     for key,val in has2.items():
# #         if val ==maxi:
# #             ls.append(key)
# #     print(min(ls))


# # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^666")

# # from collections import Counter
# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     hashmap = Counter(map(int,input().split()))
# #     newMap = {}
# #     narr = []
# #     newMap = Counter(hashmap.values())
# #     maxi = max(newMap.values())
# #     narr = [int(key) for key,val in newMap.items() if val == maxi]
# #     print(min(narr))

# for i in range(int(input())):
#     s = sorted(input())
#     p = sorted(input())
#     ns =""
#     for i in p:
#         for j in s:
#             if i!=j:
#                 ns+=j
#     #print(ns)
#     a = 0
#     for i in s:
#         if p[0]>i:
#             break
#         else:
#             a+=1
#     #print(ord())
#     print("a"<"b")
#     print(a)
#     print(p)
#     print(ns)
#    print("".join(ns[:a:])+p+ns[:a+1:])
# for i in range(int(input())):
#     user = input()
#     ls = list(map(int, input().split()))
#     a = ls.index(max(ls))
#     print(len(ls[a::]))

'''codeforcse'''
for i in range(int(input())):
    n =int(input())
    ls =[]
    for i in range(n):
        ls+=input()
    ss =set(ls)
    for i in ss:
        if ls.count(i)%n != 0:
            print("NO")
            break
    else:
        print("YES")

# def choices():
#    arry =["1.Check Set is Empty.","2.Check Whether Set is Equal.","3.Check Whether Set is Finite or Infinite.","4.Check Whether Given Set is Subset","5.Find Difference with Set","6.Check Whether SuperSet."]
#    for i in arry:
#       print(i)
#    return arry

# def setfuntion():
# 	print("Enter Set1 Elemens")
# 	set1 = set(map(int, input().split()))
# 	print(f"set is :{set1}\n")
# 	run = True
# 	while  run:
# 		choices()
# 		option = int(input("Enter your option:"))
# 		if option == 1:
# 			print("Empty..!"if len(set1)==0 else"Not Empty..!")
# 		elif option== 2:
# 			print("Enter Set 2:")
# 			set2 = set(map(int, input().split()))
# 			print("Equal set"if set1== set2 else " Not Equal")
# 		elif option == 3:
# 			print("Finite")
# 		elif option== 4:
# 			print("Enter Set 2:")
# 			set2 = set(map(int, input().split()))
# 			print("Yes"if set2.issubset(set1) else "No")
# 		elif option ==5:
# 			print("Enter set 2:")
# 			set2 = set(map(int, input().split()))
# 			print("Set diff is :",set1.difference(set2))
# 		elif option == 6:
# 			print("Entet set 2:")
# 			set2 = set(map(int, input().split()))
# 			print("Yes"if set2.issuperset(set1)else "No")
# 		else:
# 			print("Please Select Valid Option !")
# 		print("Do Want To Continue(y/n)")
# 		user = input()
# 		if user.lower()== "y":
# 			run =True
# 		else:
# 			run = False
# 	print("TANKYOU FOR USING OUR PROGRAM")
# setfuntion()
ls =[1,2,3,4,5]
print(ls[:0:-1],ls[:1:])
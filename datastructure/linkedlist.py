'''Simple Opretion on liknked list using some basic funtion '''

class Node:
	def __init__(self, data, next= None):
		self.data = data 
		self.next = next
#linked list classs
class linkedlist:
	def __init__(self):
		self.head = None
	
	#fuction for inserting the nodes to linked list 
	def insertt(self, data):
		newnode = Node(data)
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = newnode
		else:
			self.head = newnode
	#delet node from list 
	def dltt(self, postion):
		current = self.head
		currentpos = 1
		#2 because 1st note pointers next points to None 
		if postion <=0:
			if current.next is not None:
				self.head = current.next
				current =None
				return
			else:
				self.head = None
				print("linked list is empt")
				return
		else:
			while currentpos<postion:
				if currentpos == postion:
					current.next = current.next.next
					current =None
					break
				else:
					if current.next is not None:
						current = current.next
						currentpos+=1
					else:
						break
			else:
				print("Position Not Found.!")

		
	#print linked list 
	def printll(self):
		current = self.head 
		while current:
			print(current.data, end="--> ")
			current = current.next

ll = linkedlist()
ll.insertt(1)
ll.insertt(2)
ll.insertt(3)
ll.insertt(4)
ll.insertt(5)
ll.dltt(0)
ll.printll()
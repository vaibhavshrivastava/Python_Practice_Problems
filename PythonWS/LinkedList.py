# Definition for singly-linked list.

class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList:
	def __init__(self,n):
		self.head=n
	
	def AddToList(self,n):
		current =self.head
		if current is None:
			self.head=current=n
		else:
			while(current.next is not None):
				current=current.next
			current.next=n
	
	def PrintList(self):
		if(self.head is None):
			print("None")
		else:
			current=self.head
			while(current is not None):
				print(current.val)
				current=current.next

	def reverseList(self):
		if self.head.next is None:
			return self.head
		prev = None
		current=self.head
		while(current is not None):
			temp = current.next
			current.next = prev
			prev = current 
			current = temp
		return prev

	def RemoveDuplicates(self):
		if(self.head.next is None):
			return self.head
		prev = self.head
		current = prev.next
		while current is not None:
			if prev.val == current.val:
				current = current.next
				prev.next = current
			else:
				current = current.next
				prev=prev.next

	def RemoveDuplicates2(self,A):
		if A is None or A.next is None :
			return A
		if A.val != A.next.val:
			A.next=self.RemoveDuplicates2(A.next)
			return A
		else:
			tracker = Node(0)
			tracker = A
			while tracker is not None and tracker.val == A.val:
				tracker = tracker.next
			return self.RemoveDuplicates2(tracker)

	def mergeTwoLists(self,A,B):
		head=current=Node(None)
		while A is not None and B is not None :
			if A.val < B.val:
				current.next = A
				current = current.next
				A = A.next
			else :
				current.next = B
				current=current.next
				B = B.next
		if A:
			current.next = A
		elif B:
			current.next = B

		return head.next
	
	def removeNthFromEnd(self, A, B):
		if A is None or A.next is None:
			return None
		slow = fast = A
		for i in range (0, B+1):
			if fast.next is None:
				fast=A
			else:
				fast= fast.next
		while fast is not None:
			slow = slow.next
			fast = fast.next
		slow.next = slow.next.next
		return A

	def rotateRight(self, A, B):
		fast = slow = A
		
		for x in range(0,B):
			fast=fast.next
			
		while fast.next:
			fast=fast.next
			slow=slow.next
		
		fast.next=A
		A=slow.next
		slow.next=None
		return A
	def reverseBetween(self, A, B, C):
		prev = Node(None)
		prev.next = A
		count = 1
		current = A
		start = end = A
		while current:
			if count == B:
				start = current
				while count<= C:
					temp = current.next
					current.next = prev
					prev = current 
					current = temp
					
			prev.next= current
			current= current.next
			


				



				


				  

o = Node(1)
l1=LinkedList(o)
l1.AddToList(Node(3))
l1.AddToList(Node(5))
l1.AddToList(Node(7))
l1.AddToList(Node(9))

e = Node (2)
l2= LinkedList(e)
l2.AddToList(Node(4))
l2.AddToList(Node(6))
l1.PrintList()
print("-------")

result=l1.rotateRight(o,2)
#result=l1.removeNthFromEnd(o,2)
#result = l1.mergeTwoLists(o,e)

while(result is not None):
	print(result.val)
	result= result.next

















		



'''
Time Complexity: This approach takes the worst time complexity of O(n^2)
'''

def insert_at_bottom(stack,value):
    if len(stack)==0:
        stack.append(value)
        return 
    element=stack.pop()
    insert_at_bottom(stack,value)
    stack.append(element)
    return 
    
def reverse(stack):
    if len(stack)==0:
        return 
    value=stack.pop()
    reverse(stack)
    
    insert_at_bottom(stack,value)
    return 

stack=[]
stack.append(5)
stack.append(4)
stack.append(3)
stack.append(2)
stack.append(1)

print(stack,'Original stack')
reverse(stack)
print(stack,'Reversed Stack')


'''
Time Complexity: This approach takes the worst time complexity of O(n)
'''

class StackNode:
	
	def __init__(self, data):
		
		self.data = data
		self.next = None

class Stack:
	
	def __init__(self):
		
		self.top = None
		self.curr=None
	
	# Push and pop operations
	def push(self, data):
	
		if (self.top == None):
			self.top = StackNode(data)
			self.curr=self.top
			return
		
		s = StackNode(data)
		self.curr.next=s
		self.curr=s
		#self.top = s
	
	def pop(self):
	
		s = self.top
		self.top = self.top.next
		return s

	# Prints contents of stack
	def display(self):
	
		s = self.top
		
		while (s != None):
			print(s.data, end = ' ')
			s = s.next
		
	# Reverses the stack using simple
	# linked list reversal logic.
	def reverse(self):

		prev = None
		cur = self.top
		
		while (cur != None):
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		
		self.top = prev
	
# Driver code
if __name__=='__main__':
	
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	
	print("Original Stack")
	s.display()
	print()
	
	# Reverse
	s.reverse()

	print("Reversed Stack")
	s.display()
	
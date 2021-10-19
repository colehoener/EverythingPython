import sys

#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list
class Stack:
	#Create a New Empty Stack
	def __init__(self):
		self.__S = []
	#Display the Stack
	def __str__(self):
		return str(self.__S)
	#Add a new element to top of stack
	def push(self,x):
		self.__S.append(x)
	#Remove the top element from stack
	def pop(self):
		return self.__S.pop()
	#See what element is on top of stack
	#Leaves stack unchanged
	def top(self):
		return self.__S[-1]

def postfix(exp):
	stk = Stack()

	listEq = [k for k in exp.split(' ')]

	#print(listEq)

	for value in listEq:
		#print(value)
		
		try:
			int(value)
			stk.push(value)
		except ValueError:
			#print("ran")
			op1 = int(stk.pop())
			op2 = int(stk.pop())
            
			if value == '+':
				result = op1 + op2
				#print("added")
			elif value  == '-':
				result = op2 - op1
			elif value == '*':
				result = op1 * op2
			elif value == '/':
				result = op2 / op1

			stk.push(result)
			#print(stk)

	return(float(stk.pop()))


#main
print("Welcome to Postfix Calculator")

print("Enter exit to quit.")

while(True):
	exp = input("Enter Expression:\n")

	if(exp != "exit"):
		result = postfix(exp)
		print("Result:", result)
	else:
		sys.exit()


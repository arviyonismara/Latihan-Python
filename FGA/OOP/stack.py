# stack dengan prosedural approach
stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)
print(stack)
pop()
print(stack)

# Stack oop

class Stack:
	def __init__(self):
		print("Hallo")
		pass

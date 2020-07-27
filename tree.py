# creation binary tree 
class Node:

	# initialize node with it's data value and with left right values to be null
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
	# insert in the node
	def insert(self, data):
		if self.data:
				if data < self.data: # go left
					if self.left: 
						self.left.insert(data)
					else:
						# create Node
						self.left = Node(data)
				
				else: # go right
					if self.right:
						# Node is created already, so insert the value in the node
						self.right.insert(data)
					else:
						# create Node
						self.right = Node(data)

		else:
			self.data = data


# preorder traversal 
def preorder_traversal(root):
	# first print the data of the current node
	# then go left
	# then go right
	if root:
		print(root.data) 
		preorder_traversal(root.left) 
		preorder_traversal(root.right)
			
def postorder_traversal(root):
	if root:
		preorder_traversal(root.left) 
		preorder_traversal(root.right)
		print(root.data) 
			
def inorder_traversal(root):
	if root:
		preorder_traversal(root.left) 
		print(root.data) 
		preorder_traversal(root.right)

n = Node(12)
n.insert(5)
n.insert(1)
n.insert(10)
n.insert(21)
n.insert(14)

#print(n)
print('-----------------')
postorder_traversal(n)
print('-----------------')
inorder_traversal(n)
print('-----------------')
preorder_traversal(n)

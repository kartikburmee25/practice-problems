class Node:
	
	def __init__(self, data):
		self.info = data
		self.left = None
		self.right = None

class Tree:
	
	def __init__(self):
		self.root=None

	def create(self, data):
		if self.root==None:
			self.root=Node(data)
		else:
			current=self.root

			while True:
				if data<current.info:
					if curent.left:
						current=current.left
					else:
						current.left=Node(data)
						break
				elif data >= current.info:
					if current.right:
						current=current.right
					else:
						current.right=Node(data)
						break
				else:
					break
	
	def print_inorder(root):
		if root==None:
			return
		print_inorder(root.left)
		print(root.info)
		print_inorder(root.right)


def main():
	list_of_elements=[4,2,9,1,67,87,3,2,5,5,0]
	bst=Tree()
	for x in list_of_elements:
		bst.create(x)
	bst.print_inorder(bst.root)



if __init__=='__main__':
	
	main()
	
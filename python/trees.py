class Node:
	
	def __init__(self, data):
		self.info = data
		self.left = None
		self.right = None

class BSTree:
	
	def __init__(self):
		self.root=None
		self.count_min_tree_calls=0
		self.count_inorder_calls=0
		self.count_preorder_calls=0
		self.prev=None
	def insert_node(self, data):
		if self.root==None:
			self.root=Node(data)
		else:
			current=self.root

			while True:
				if data<current.info:
					if current.left:
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

	def create_min_tree(self, list_of_nodes):
		if not list_of_nodes:
			return None
		middle=int(len(list_of_nodes)/2)
		root=Node(list_of_nodes[middle])
		print(str(root.info))
		root.left=self.create_min_tree(list_of_nodes[:middle])
		root.right=self.create_min_tree(list_of_nodes[middle+1:])
		self.count_min_tree_calls+=1
		return root


	def print_inorder(self,root):
		if root==None:
			return
		self.print_inorder(root.left)
		print(root.info)
		self.print_inorder(root.right)
		self.count_inorder_calls+=1

	def print_preorder(self,root):
		if root==None:
			return
		print(root.info)
		self.print_preorder(root.left)
		self.print_preorder(root.right)
		self.count_preorder_calls+=1

	def height(self, root):
		if root==None:
			return 0
		if self.height(root.left)>=self.height(root.right):
			return self.height(root.left)+1
		else:
			return self.height(root.right)+1

	def is_balanced(self, root):
		if root==None:
			return True
		if abs(self.height(root.left)-self.height(root.right))<=1 and self.is_balanced(root.left) is True and self.is_balanced(root.right) is True:
			return True
		return False

	def level_order(self, root, height):
		if height==1:
			print (root)
		self.level_order(root.left, height-1)
		self.level_order(root.right, height-1)

	def bst_helper(self,root,min_val,max_val):
		if root==None:
			return True
		if root.info<=min_val or root.info>=max_val:
			return False
		l=self.bst_helper(root.left,min_val,root.info)
		r=self.bst_helper(root.right,root.info,max_val)
		return (l and r)


	def validate_bst_tree(self, root):
		return self.bst_helper(root,float("-inf"),float("inf"))

	def print_leaves(self,root):
		if root==None:
			return
		if root.left==None and root.right==None:
			print (root.info)
		self.print_leaves(root.left)
		self.print_leaves(root.right)





def main():
	bst=BSTree()
	#root = bst.create_min_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
	#print("\n\n{}\n".format(bst.count_min_tree_calls))
	#for x in list_of_elements:
	#	bst.insert_node(x)
	#bst.print_preorder(root)
	#print("\n\n{}\n".format(bst.count_preorder_calls))
	#print(bst.height(root))
	root = Node(20)
	root.left = Node(30)
	root.left.left=Node(10)
	root.right=Node(19)
	root.right.left=Node(2)
	is_bst = bst.validate_bst_tree(root,root.info)
	print(is_bst)



if __name__=='__main__':
	
	main()
	
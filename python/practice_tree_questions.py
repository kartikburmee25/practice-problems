import trees
import os

bst = trees.BSTree()
root = bst.root

root = bst.create_min_tree([1,2,3,4,5,6,7,8,9,10,11,12,13])
bst.print_inorder(root)
print (bst.is_balanced(root))
max=0

print (bst.validate_bst_tree(root))
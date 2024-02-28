from binarytree import build,bst

nodes = [10,5,4,20,47, None, 67]

binary_tree = build(nodes)
binary_tree = bst(height=3,is_perfect=True)


print("Binary Tree from the list:\n", binary_tree)


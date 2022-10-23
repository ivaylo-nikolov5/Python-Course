from binary_search_tree import BinarySearchTree

tree = BinarySearchTree()
tree.insert(100)
tree.insert(50)
tree.insert(25)
tree.insert(75)
tree.insert(150)
tree.insert(125)
tree.insert(175)


print(tree.get_min_value())
print(tree.get_max_value())
tree.traverse()
tree.remove(100)
tree.traverse()
from demo import BinarySearchTree

bsr = BinarySearchTree()
bsr.insert(100)
bsr.insert(50)
bsr.insert(120)
bsr.insert(20)
bsr.insert(45)
bsr.insert(260)
bsr.insert(76)


print(bsr.is_exists(100))
print(bsr.is_exists(20))
print(bsr.is_exists(220))


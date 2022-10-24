class Node:
    def __init__(self, value):
        self.value = value
        self.left_value = None
        self.right_value = None


class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.vals = []

    def insert(self, value):
        if not self.__root:
            self.__root = Node(value)
            return print("Inserted value as root...")
        return self.__insert_node(self.__root, value)

    def __insert_node(self, node, value):
        if value < node.value:
            if node.left_value:
                return self.__insert_node(node.left_value, value)
            node.left_value = Node(value)
        else:
            if node.right_value:
                return self.__insert_node(node.right_value, value)
            node.right_value = Node(value)
            return

    def traverse(self):
        if not self.__root:
            return "You cannot traverse an empty binary searching tree!"
        self.__traverse_in_order(self.__root)

    def __traverse_in_order(self, node):
        if node.left_value:
            self.__traverse_in_order(node.left_value)

        print(node.value)

        if node.right_value:
            self.__traverse_in_order(node.right_value)


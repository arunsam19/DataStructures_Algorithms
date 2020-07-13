
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is not None:
            if self.value > value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def display_pre_order(self):
        print(str(self.value))
        if self.left is not None:
            self.left.display_pre_order()
        if self.right is not None:
            self.right.display_pre_order()


    def display_in_order(self):
        if self.left is not None:
            self.left.display_pre_order()
        print(str(self.value))
        if self.right is not None:
            self.right.display_pre_order()


    def display_post_order(self):
        if self.left is not None:
            self.left.display_pre_order()
        if self.right is not None:
            self.right.display_pre_order()
        print(str(self.value))

if __name__ == "__main__":
    root = Node(4)
    root.insert(5)
    root.insert(6)
    root.insert(3)
    root.insert(2)
    root.insert(1)
    root.insert(7)

    # Pre-order traversal
    print("Traversing the Binary search tree in Pre-order:")
    root.display_pre_order()

    # In-order traversal
    print("Traversing the Binary search tree in In-order:")
    root.display_in_order()

    # Post-order traversal
    print("Traversing the Binary search tree in Post-order:")
    root.display_post_order()
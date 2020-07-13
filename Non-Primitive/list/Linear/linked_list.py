class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """insert new node to be the head"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current = self.head
        stringoutput = ""
        while current:
            stringoutput += str(current.value)
            current = current.next
        return stringoutput

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_before(self, value, newVal):
        current = self.head
        if current.value == value:
            new_node = Node(newVal)
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next:
                if current.next.value == value:
                    new_node = Node(newVal)
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next

    def insert_after(self, value, newVal):
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(newVal)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def kth_from_end(self, k):
        current = self.head
        while current:
            if current.value == k:
                kNode = current
                break
            current = current.next
        current = kNode
        i = 0
        while current:
            current = current.next
            i += 1
        #print("The node with value {} is {}th element from end".format(k, i))
        print("The node with value %d is %dth element from end" % (k, i))

    def remove_node(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            current.next = None
            return
        while current.next.value != value:
            current = current.next
        current.next = current.next.next
        current.next.next = None


if __name__ == "__main__":
    lst1 = Linked_list()
    lst1.insert(1)
    lst1.append(2)
    lst1.append(3)
    lst1.append(4)
    lst1.append(5)
    lst1.append(7)
    lst1.append(6)
    print(lst1.to_string())
    # print(lst1.to_string())
    print("lst1 in string: " + lst1.to_string())
    lst1.insert_after(2, 90)
    print("lst1 in string after inserting 420 after 2: " + lst1.to_string())
    lst1.insert_before(5, 9)
    print("lst1 in string after inserting 11 before 5: " + lst1.to_string())
    lst1.kth_from_end(3)
    # print(lst.includes('a'))
    # print(lst.includes(1))
    lst1.remove_node(7)
    print(lst1.to_string())



















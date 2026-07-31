class Node:
    """
    Represents a single node int he linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Represents the linked list structure
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Add a new node to the end of the list
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        """
        Print the entire linked list
        """
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) if elements else "Empty List")


list1 = Node(1)
ll = LinkedList()

ll.append(1)
ll.append(2)

ll.display()

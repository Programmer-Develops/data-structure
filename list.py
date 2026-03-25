# Singly Linked List

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None
        
        # insert at start
        def insert_at_start(self,x):
            new_node = Node(x)
            new_node.next = self.head()
            self.head = new_node
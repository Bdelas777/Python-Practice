# Python Script to Practice Manipulation of a Doubly Linked List

# Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Insert method   
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    # Delete method
    def delete(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                return
            current_node = current_node.next
            
    # Display method
    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print('END')

# Create a doubly linked list
dList = DoublyLinkedList()

# Insert some elements into the doubly linked list
dList.insert('Mars')
dList.insert('Jupiter')
dList.insert('Saturn')

# Remove a node from the doubly linked list
dList.delete('Jupiter')

# Display the elements of the doubly linked list
dList.display_forward()  # Existing output: Mars <-> Saturn <-> END
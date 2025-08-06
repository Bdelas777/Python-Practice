class Node:
   def __init__(self, value):
       self.value = value
       self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
       self.tail = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
    
    # Defining the delete method
    def delete(self, value):
        temp = self.head
        if (temp is not None):
            if temp.value == value:
                self.head = temp.next
                temp = None
                return
            while (temp is not None):
                if temp.value == value:
                    break
                prev = temp
                temp = temp.next
            if temp is None:
                return
            prev.next = temp.next
            temp = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" => ")
            temp = temp.next
        print("None")

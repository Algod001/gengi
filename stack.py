class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        current = self.head
        self.head = new_element
        new_element.next = current

    def delete_first(self):
   
        if self.head:
            deleted_element = self.head
            self.head = deleted_element.next
            deleted_element.next = None
            return deleted_element

class Stack:
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):

        current = self.ll.head
        self.ll.head = new_element
        new_element.next = current

    def pop(self):
        return self.ll.delete_first()


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
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

    def get_position(self, position):
        if position < 1:
            return None
        current = self.head
        for i in range(1, position):
            if current.next:
                current = current.next
            else:
                return None
        return current

    def insert(self, new_element, position):
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            prev = self.get_position(position - 1)
            if prev:
                new_element.next = prev.next
                prev.next = new_element

    def delete(self, value):
        current = self.head
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

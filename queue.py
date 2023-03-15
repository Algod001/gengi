class elements:
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue:
    def __init__(self, head=None):
        self.storage = elements(head)

    def enqueue(self, new_element):
        if self.storage:
            current = self.storage
            while current.next:
                current = current.next
            current.next =elements(new_element)
        else:
            self.storage = elements(new_element)

    def peek(self):
        return self.storage.value

    def dequeue(self):
        if self.storage:
            current = self.storage
            self.storage= current.next
            return current.value
        else:
            return None


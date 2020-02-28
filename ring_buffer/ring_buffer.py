from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # Length is none, insert 0th element, initialize pointer
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

            if self.storage.length == self.capacity:
                if self.current is not self.storage.head:
                    self.storage.remove_from_head()
                    self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Index 0 was out of bounds?
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
            return
        self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        return [x for x in self.storage if x]


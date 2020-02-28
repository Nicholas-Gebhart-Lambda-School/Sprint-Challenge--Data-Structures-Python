import sys
# from dll_stack import Stack
# from dll_queue import Queue
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                    return
                self.left = BinarySearchTree(value)
                return
            if self.right:
                self.right.insert(value)
                return
            self.right = BinarySearchTree(value)
            return
        self.value = value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        """
        Angry Linter
        """
        if self.value:
            if target == self.value:
                return True
            if target <= self.value and self.left:
                return self.left.contains(target)
            if target >= self.value and self.right:
                return self.right.contains(target)
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        if self.value <= self.right.value:
            return self.right.get_max()


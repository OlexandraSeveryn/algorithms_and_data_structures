from algorithms.SecondPractice.practice import Penguin


class Node:

    def __init__(self, data: Penguin):
        self.data = data    #type: Penguin
        self.next = None    #type: [Node, None]

    def has_value(self, value: Penguin):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data

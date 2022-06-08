from algorithms.SecondPractice.practice import Penguin
from algorithms.SecondPractice.practice import Generator
from AbstractStructure import AbstractStructure


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_value(self, value: Penguin):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data


class LinkedList(AbstractStructure):
    __head: [None, Node] = Node
    __tail: [None, Node] = Node
    size: int = 0

    def add(self, value: Penguin, index: [int, None] = None) -> bool:
        if index is not None and (index < 0 or index > self.size):
            return False
        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
            self.size += 1
        elif index is None:
            current = self.__tail
            node = Node(value)
            current.next = node
            self.__tail = node

            # current = self.__head
            # while current.next:
            #     current = current.next
            # current.next = Node(value)
            self.size += 1
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
            self.size += 1
        return True

    def insert(self, value: Penguin, index: [int, None] = None):
        if index is not None and (index < 0 or index >= self.size):
            return True
        else:
            i = 0
            current = self.__head
            while i < index - 1 and current is not None:
                i += 1
                current = current.next
            node = Node(value)
            node.next = current.next
            current.next = node
        return False

    def find(self, value: Penguin):
        current = self.__head
        i = 0
        try:
            while current is not None:
                i += 1
                current = current.next
            return i
        except:
            return None

    def get(self, index: [str, int]) -> object:
        if self.size <= index or index < 0:
            return None
        else:
            i = 0
            current = self.__head
            while current.next and i < index:
                current = current.next
                i += 1
            return current.data

    def remove(self, value: Penguin) -> bool:
        current = self.__head
        if current is None:
            return False
        while current:
            try:
                if current.next.data == value:
                    current.next = current.next.next
                    break
            except:
                pass
            if current.data == value:
                self.__head = current.next
                break
            current = current.next
        self.size -= 1
        return True

    def get_all(self) -> list:
        out = []
        current_elem = self.__head
        while current_elem is not None:
            out.append(current_elem.data)
            current_elem = current_elem.next
        return out


if __name__ == "__main__":

    gen = Generator()

    penguin1 = gen.generate_single()
    penguin2 = gen.generate_single()
    penguin3 = gen.generate_single()
    penguin4 = gen.generate_single()
    penguin5 = gen.generate_single()
    print("все пингвины:", [penguin1, penguin2, penguin3, penguin4, penguin5])
    link_list = LinkedList()
    print("----- method add-----")
    print("add_1: " + str(link_list.add(penguin1)))
    print("add_2: " + str(link_list.add(penguin2)))
    print("add_3: " + str(link_list.add(penguin3)))
    print("add_4: " + str(link_list.add(penguin4)))
    print("add: " + str(link_list.add(penguin5, 1)))
    print("-----method insert-----")
    print("insert: " + str(link_list.insert(penguin3, 2)))
    print("-----method find-----")
    print("find: " + str(link_list.find(penguin1)))
    print("get all: " + str(link_list.get_all()))
    print("size: " + str(link_list.size))
    print("-----method get-----")
    print("get_1: " + str(link_list.get(3)))
    print("get_1: " + str(link_list.get(0)))
    print("-----method remove-----")
    print("remove penguin 3: " + str(link_list.remove(penguin3)))
    print("find: " + str(link_list.find(penguin3)))
    print("-----THE END-----")

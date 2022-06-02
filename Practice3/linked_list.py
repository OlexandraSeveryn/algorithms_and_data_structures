from AbstractStructure import AbstractStructure
from algorithms.SecondPractice.practice import Penguin
from algorithms.SecondPractice.practice import Generator
from node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = Node
    __tail: [None, Node] = Node
    size: int = 0

    def add(self, value: Penguin, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False

        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
            self.size += 1
        elif index is None:
            # variant 1
            # current_elem = self.__head
            # while current_elem.next:
            #    current_elem = current_elem.next
            # node = Node(value)
            # current_elem.next = node

            # variant 2
            current_elem = self.__tail
            node = Node(value)
            current_elem.next = node
            self.__tail = node
            self.size += 1
        else:
            i = 0
            current_elem = self.__head
            while current_elem.next and i < index - 1:
                current_elem = current_elem.next
                i += 1
            node = Node(value)
            node.next = current_elem.next
            current_elem.next = node
            self.size += 1
        return True

    def insert(self, value, index) -> bool:
        pass

    def find(self, value) -> [int, None]:
        pass

    def get(self, index) -> object:
        pass

    def remove(self, value) -> bool:
        # current_elem.next.data == value
        # current_elem.next = current_elem.next.next

        pass

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
    print([penguin1, penguin2, penguin3, penguin4, penguin5])

    s_list = LinkList()
    s_list.add(penguin1)
    s_list.add(penguin2)
    s_list.add(penguin4)
    s_list.add(penguin5, 2)
    # print("insert_1: " + str(s_list.insert(penguin4, 1)))
    # print("insert_2: " + str(s_list.insert(penguin4, 10)))

    print(s_list.get_all())
    print(s_list.size)
    # print(len(s_list))

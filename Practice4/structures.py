from algorithms.Practice4.AbstractLimitStructure import AbstractQueue, AbstractStack
from algorithms.SecondPractice.practice import Generator, Penguin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(AbstractStack):
    __list = []
    __head: Node = None

    def push(self, value: Penguin):
        self.__list.append(value)

        node = Node(value)
        node.next = self.__head

    def pop(self) -> (Penguin, None):
        if self.__head is not None:
            head = self.__head
            top = head.n
            new_top = top.n
            head.n = new_top
            return top.data
        else:
            return None

    def top(self) -> (Penguin, None):
        if self.__head is not None:
            return self.__head.data
        else:
            return None

    def __len__(self):
        return len(self.__list)

    def get_all(self):
        return self.__list.copy()


class Queue(AbstractQueue):
    __list = []
    __size = 0

    def enqueue(self, value: Penguin):
        self.__list.append(value)
        self.__size += 1
        return True

    def dequeue(self) -> (Penguin, None):
        if self.__size != 0:
            value = self.__list[0]
            self.__list.remove(value)
            self.__size -= 1
            return value
        else:
            return None

    def top(self) -> (Penguin, None):
        if self.__size != 0:
            return self.__list[0]
        else:
            return None

    def __len__(self):
        return len(self.__list)

    def get_all(self):
        return self.__list.copy()


if __name__ == '__main__':
    gen = Generator()

    print('-' * 10, 'stack', '-' * 10)

    stack = Stack()
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())

    lst1 = stack.get_all()
    print(str(lst1))
    lst1.remove(lst1[1])
    print(str(lst1))
    lst1 = stack.get_all()
    print(str(lst1))

    print('-' * 10, 'deque', '-' * 10)

    lst2 = [gen.generate_single() for i in range(5)]
    print(lst2)

    queeue = Queue()
    for item in lst2:
        queeue.enqueue(item)
    print(queeue.get_all())

    queeue.dequeue()
    queeue.dequeue()
    print(queeue.get_all())
    print(len(queeue))

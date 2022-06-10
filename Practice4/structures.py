from algorithms.Practice4.AbstractLimitStructure import AbstractQueue, AbstractStack
from algorithms.SecondPractice.practice import Generator, Penguin
from collections import deque


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

    def pop(self) -> Penguin:
        return self.__list.pop()

    def top(self) -> Penguin:
        return self.__list[-1]

    def __len__(self):
        return len(self.__list)

    def get_all(self):
        return self.__list.copy()


class Queue(AbstractQueue):
    __list = []

    def enqueue(self, value: Penguin):
        self.__list.append(value)

    def dequeue(self) -> Penguin:
        return self.__list.pop(0)

    def top(self) -> Penguin:
        return self.__list[0]

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

    print('-' * 10, 'queue', '-' * 10)

    lst2 = [gen.generate_single() for i in range(5)]
    print(lst2)

    queue = Queue()
    for item in lst2:
        queue.enqueue(item)
    print(queue.get_all())

    queue.dequeue()
    queue.dequeue()
    print(queue.get_all())
    print(len(queue))

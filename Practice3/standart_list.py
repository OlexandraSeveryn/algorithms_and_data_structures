from AbstractStructure import AbstractStructure
from algorithms.SecondPractice.practice import Penguin
from algorithms.SecondPractice.practice import Generator


class List(AbstractStructure):
    __list: list = []
    size: int = 0

    def add(self, value: Penguin, index: [int, None] = None) -> bool:
        if index is None:
            self.__list.append(value)
            self.size += 1
            return True
        elif self.size > index > -self.size:
            self.__list.insert(index, value)
            self.size += 1
            return True
        else:
            return False

    def insert(self, value: Penguin, index: int) -> bool:
        if index is None or index < -self.size or index >= self.size:
            return False
        self.__list[index] = value
        return True

    def find(self, value: Penguin) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        return None

    def get(self, index: int) -> [Penguin, None]:
        if -self.size <= index < self.size:
            return self.__list[index]
        return None

    def remove(self, value: Penguin) -> bool:
        try:
            self.__list.remove(value)
            self.size -= 1
            return True
        except ValueError:
            return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self):
        return self.size


if __name__ == "__main__":

    gen = Generator()

    penguin1 = gen.generate_single()
    penguin2 = gen.generate_single()
    penguin3 = gen.generate_single()
    penguin4 = gen.generate_single()
    penguin5 = gen.generate_single()
    print([penguin1, penguin2, penguin3, penguin4])

    s_list = List()
    print("add_1: " + str(s_list.add(penguin1)))
    print("add_2: " + str(s_list.add(penguin2)))
    print("add_3: " + str(s_list.add(penguin3)))
    print("add_4: " + str(s_list.add(penguin4)))
    print("insert: " + str(s_list.insert(penguin5, 1)))
    print("get_all1: " + str(s_list.get_all()))
    print("len: " + str(len(s_list)))
    print("find_1: " + str(s_list.find(penguin1)))
    print("find_2: " + str(s_list.find(penguin2)))
    print("get: " + str(s_list.get(0)))
    print("remove_1: " + str(s_list.remove(penguin2)))
    print("remove_2: " + str(s_list.remove(penguin2)))
    print("get_all2: " + str(s_list.get_all()))
    print("len_2: " + str(len(s_list)))

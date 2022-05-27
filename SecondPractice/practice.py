import names
import random


class Penguin:
    name: str
    breed: str
    size: str
    areal: str
    flying: str

    def __init__(self, name: str, breed: str, size: str, areal: str, flying: str = "не умеет летать"):
        self.name = name
        self.breed = breed
        self.size = size
        self.areal = areal
        self.flying = flying

    def get_info(self) -> str:

        return f'Пингвин {self.name}, породы {self.breed}, вырастает до {self.size} см ' \
               f'и относится к {self.get_size()}. Обитает в {self.get_areal()} ' \
                f'регионе, а также {self.flying}'

    def __repr__(self) -> str:
        return f'Penguin {self.name} {self.breed} {self.size} {self.areal} {self.flying}'

    def get_size(self) -> str:
        if self.size >= str(100):
            return "крупным"
        elif str(100) > self.size >= str(70):
            return "большим"
        elif str(70) > self.size >= str(50):
            return "средним"
        else:
            return "небольшим"

    def get_areal(self) -> str:
        if self.areal == "Северная Америка" and "Южная Америка":
            return "американском"
        elif self.areal == "Европа" and "Азия":
            return "европоазиатском"
        elif self.areal == "Африка":
            return "африканском"
        elif self.areal == "Австралия":
            return "австралийском"
        elif self.areal == "Арктика":
            return "арктическом"
        elif self.areal == "Антарктида":
            return "антарктическом"
        assert False


class Generator:

    def __create_breed(self) -> str:
        self.breed = random.choice(['хохлатый', 'королевский', 'арктический', 'малый'])
        return self.breed

    def __create_sizes(self):
        self.size = random.randint(20, 250)
        return self.size

    def __create_size(self) -> str:
        if self.size >= int(100):
            return "крупным"
        elif int(100) > self.size >= int(70):
            return "большим"
        elif int(70) > self.size >= int(50):
            return "средним"
        else:
            return "небольшим"

    def __create_area(self) -> str:
        self.area = random.choice(['Северная Америка', 'Южная Америка', 'Европа', 'Азия',
                                   'Австралия', 'Арктика', 'Африка'])
        return self.area

    def __create_areal(self) -> str:
        if self.area == "Северная Америка":
            return "американском"
        elif self.area == "Южная Америка":
            return "американском"
        elif self.area == "Европа":
            return "европоазиатском"
        elif self.area == "Азия":
            return "европоазиатском"
        elif self.area == "Африка":
            return "африканском"
        elif self.area == "Австралия":
            return "австралийском"
        elif self.area == "Арктика":
            return "арктическом"
        assert False

    def __create_flying(self) -> str:
        self.flying = random.choice(['умеет летать', 'не умеет летать'])
        return self.flying

    def generate_single(self):
        name = names.get_first_name()
        return [name, self.__create_breed(), self.__create_sizes(), self.__create_size(), self.__create_area(),
                self.__create_areal(), self.__create_flying()]

    def generate_1000(self) -> list:
        penguinlist = list()
        for i in range(1001):
            penguinlist.append(self.generate_single())
        return penguinlist

    def generate_10000(self) -> list:
        penguinlist = list()
        [penguinlist.append(self.generate_single()) for i in range(10000)]
        return penguinlist


if __name__ == "__main__":
    penguin = Penguin("Шкипер", "королевский", str(60), "Европа")
    print(penguin.get_info())

    penguin = Penguin("Ковальски", "хохлатый", str(105), "Северная Америка")
    print(penguin.get_info())

    penguin = Penguin("Рико", "антарктический", str(80), "Арктика")
    print(penguin.get_info())

    g = Generator()
    print(g.generate_single())

    print(g.generate_1000())

    print(g.generate_10000())

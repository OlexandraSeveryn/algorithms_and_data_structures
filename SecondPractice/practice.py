import names
import random


class Penguin:
    name: str
    breed: str
    size: int
    areal: str
    flying: str

    def __init__(self, name: str, breed: str, size: int, areal: str, flying: str = "не умеет летать"):
        self.name = name
        self.breed = breed
        self.size = size
        self.areal = areal
        self.flying = flying

    def get_info(self) -> str:

        return f'Пингвин {self.name}, породы {self.breed}, вырастает до {self.size} см ' \
               f'и относится к {self.get_size()}. Обитает в {self.get_areal()} ' \
                f'регионе, а также, как и любой пингвин {self.flying}'

    def __repr__(self):
        return f'Penguin({self.name} {self.breed} {self.size} {self.areal} {self.flying})'

    def get_size(self):
        if self.size >= int(100):
            return "крупным"
        elif int(100) > self.size >= int(70):
            return "большим"
        elif int(70) > self.size >= int(50):
            return "средним"
        else:
            return "небольшим"

    def get_areal(self):
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


if __name__ == "__main__":
    penguin = Penguin("Шкипер", "королевский", 60, "Европа")
    print(penguin.get_info())

    penguin2 = Penguin("Ковальски", "хохлатый", 105, "Северная Америка")
    print(penguin.get_info())

    penguin3 = Penguin("Рико", "антарктический", 80, "Арктика")
    print(penguin.get_info())

    penguinlist = [penguin, penguin2, penguin3]
    print(penguinlist)

class Penguin:
    flying = "не умеет летать"

    def __init__(self, name, breed, size, areal):
        self.name = name
        self.breed = breed
        self.size = size
        self.areal = areal

    def get_info(self):

        return f'Пингвин {self.name}, породы {self.breed}, вырастает до {self.size} см ' \
               f'и относится к {self.get_size()}. Обитает в {self.get_areal()} ' \
                f'регионе, а также, как и любой пингвин {self.flying}'

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

    penguin = Penguin("Ковальски", "хохлатый", 105, "Северная Америка")
    print(penguin.get_info())

    penguin = Penguin("Рико", "антарктический", 80, "Арктика")
    print(penguin.get_info())

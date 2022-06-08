from algorithms.SecondPractice.practice import Generator
from standart_list import List
from linked_list import LinkedList
from datetime import datetime

generator = Generator()

# генерация новых объектов
start_time = datetime.utcnow()
generator_10000 = generator.generate_10000()
stop_time = datetime.utcnow() - start_time
print('Генерация 10000 новых элементов:\n' + str(stop_time))

# таймер добавления элементов в конец массива
start_time = datetime.utcnow()

s_list = List()
# s_list = LinkedList()
for penguin in generator_10000:
    s_list.add(penguin)
stop_time = datetime.utcnow() - start_time
print('Добавление 10000 элементов в конец массива:\n' + str(stop_time) + '\tРазмер массива: ' + str(s_list.size))

# таймер для добавления элементов в начало массива
start_time = datetime.utcnow()

# s_list = List()
# s_list = LinkedList()
for penguin in generator_10000:
    s_list.add(penguin, 0)

stop_time = datetime.utcnow() - start_time
print('Добавление 10000 элементов в начало массива:\n' + str(stop_time) + '\tРазмер массива: '
      + str(s_list.size))

# таймер для замены элемента
start_time = datetime.utcnow()

for penguin in generator_10000:
    s_list.insert(penguin, len(generator_10000) - 1)

stop_time = datetime.utcnow() - start_time
print('Последовательная замена последнего элемента 10000 значений:\n' + str(stop_time) + '\tРазмер массива: '
      + str(s_list.size))

# таймер для поиска элемента
start_time = datetime.utcnow()

result = s_list.find(generator_10000[0])

stop_time = datetime.utcnow() - start_time
print('Поиск первого элемента:\n' + str(stop_time) + '\tРазмер массива: ' + str(s_list.size))

# таймер для поиска элемента
start_time = datetime.utcnow()

stop_time = datetime.utcnow() - start_time
print('Поиск последнего элемента:\n' + str(stop_time) + '\tРазмер массива: ' + str(s_list.size))

# таймер для поиска по индексу
start_time = datetime.utcnow()

stop_time = datetime.utcnow() - start_time
print('Поиск последнего элемента из 10000 по индексу:\n' + str(stop_time) + '\tРазмер массива: '
      + str(s_list.size))

# таймер для удаления первых элементов
start_time = datetime.utcnow()

for penguin in generator_10000:
    s_list.remove(penguin)

stop_time = datetime.utcnow() - start_time
print('Удаление 1-го элемента 10000 раз:\n' + str(stop_time) + '\tРазмер массива: ' + str(s_list.size))

# таймер для удаления последних элементов
start_time = datetime.utcnow()

for penguin in reversed(generator_10000):
    s_list.remove(penguin)

stop_time = datetime.utcnow() - start_time
print('Удаление последнего элемента 10000 раз:\n' + str(stop_time) + '\tРазмер массива: ' + str(s_list.size))

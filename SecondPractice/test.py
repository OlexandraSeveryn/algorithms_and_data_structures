from practice import Penguin
from practice import Generator


def test_person():
    penguin = Penguin('some', 'example', '60', 'Африка')
    assert penguin.name == 'some'
    assert penguin.breed == 'example'
    assert penguin.size == '60'
    assert penguin.areal == 'Африка'
    assert penguin.flying == 'не умеет летать'


def test_person_full():
    penguin = Penguin('some', 'example', '70', 'Арктика')
    assert penguin.name == 'some'
    assert penguin.breed == 'example'
    assert penguin.size == '70'
    assert penguin.areal == 'Арктика'
    assert penguin.flying == 'не умеет летать'


def test_person_get_info():
    penguin = Penguin('some', 'example', '60', 'Африка')
    assert isinstance(penguin.get_info(), str)


def test_person_single_types():
    gen = Generator()
    p = gen.generate_single()
    assert isinstance(p, Penguin)
    assert isinstance(p.name, str)
    assert isinstance(p.breed, str)
    assert isinstance(p.size, str)
    assert isinstance(p.areal, str)
    assert isinstance(p.flying, str)
    assert isinstance(p.get_areal(), str)


def test_person_1000_type():
    g = Generator()
    plist = g.generate_1000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Penguin)
    assert len(plist) == 1000


def test_person_10000_type():
    g = Generator()
    plist = g.generate_10000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Penguin)
    assert len(plist) == 10000

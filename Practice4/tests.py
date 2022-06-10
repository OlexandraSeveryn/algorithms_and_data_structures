from structures import Stack
from algorithms.SecondPractice.practice import Generator, Penguin


def test_push():
    stack = Stack()
    gen = Generator()
    value = gen.generate_single()
    stack.push(value)
    assert value == stack.get_all()[0]


def test_push_type():
    stack = Stack()
    gen = Generator()
    value = gen.generate_single()
    stack.push(value)
    assert isinstance(stack.top(), Penguin)


def test_get_all():
    stack = Stack()
    gen = Generator()
    values = [gen.generate_single() for i in range(5)]
    for value in values:
        stack.push(value)
    assert values == stack.get_all()


def test_size():
    stack = Stack()
    gen = Generator()
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    assert len(stack) == 3


def test_top():
    stack = Stack()
    gen = Generator()
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    genrt = gen.generate_single()
    stack.push(genrt)
    assert stack.top() == genrt


def test_pop():
    stack = Stack()
    gen = Generator()
    stack.push(gen.generate_single())
    stack.push(gen.generate_single())
    genrt = gen.generate_single()
    stack.push(genrt)
    assert stack.pop() == genrt
    assert len(stack) == 2


def test_pop_empty():
    stack = Stack()
    assert stack.pop() == None
    assert len(stack) == 0


if __name__ == "__main__":
    G = Generator()

    # stack = Stack()
    test_push()
    # stack = Stack()
    test_get_all()
    # stack = Stack()
    test_size()

    # stack = Stack()
    test_top()

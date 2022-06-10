from datetime import datetime
from algorithms.SecondPractice.practice import Generator
from structures import Stack


class StackTime:

    def __init__(self, gen):
        self.stack = Stack()
        self.gen = gen

    def time_push(self):
        timer_start = datetime.utcnow()
        for item in self.gen:
            self.stack.push(item)
        timer_stop = datetime.utcnow() - timer_start
        print("Push 10 000 объектов:\n" + str(timer_stop))

    def time_pop(self):
        timer_start = datetime.utcnow()

        for _ in range(len(self.gen)):
            self.stack.pop()

        timer_stop = datetime.utcnow() - timer_start
        print("Pop 10 000 объектов:\n" + str(timer_stop))

    def time_top(self):
        timer_start = datetime.utcnow()

        for _ in range(len(self.gen)):
            self.stack.top()

        timer_stop = datetime.utcnow() - timer_start
        print("Top 10 000 объектов:\n" + str(timer_stop))


if __name__ == "__main__":
    G = Generator()
    gen = G.generate_10000()
    st = StackTime(gen)

    print("-------\nStack\n-------")
    st.time_push()
    st.time_top()
    st.time_pop()

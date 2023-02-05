from exercise1 import Technic


class Computer(Technic):

    def __gt__(self, other):
        return len(self.name) > len(other.name)

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    def __ge__(self, other):
        return len(self.name) >= len(other.name)

    def __le__(self, other):
        return len(self.name) <= len(other.name)


if __name__ == '__main__':
    a = Computer('makbook', 100000, True)
    b = Computer('msi', 20000, True)
    print(a > b)

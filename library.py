def squared_sum(a, b):
    sum = a + b
    squared = sum ** 2
    return squared


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Number:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def squared_sum(self):
        sum = self.__a + self.__b
        squared = sum ** 2
        return squared

    def add(self):
        return self.__a + self.__b

    def subtract(self):
        return self.__a - self.__b

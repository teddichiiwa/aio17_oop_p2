# another_library.py

def add(a, b):
    return f'{a}{b}'


# another_library.py

class String:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        return f'{self.__a}{self.__b}'

######################


def bark(target):
    return f'{target} says woof woof'


class Dog:
    def __init__(self, name, maxBarkTime=3):
        self.__timeBarked = 0               # (1)
        self.__maxBarkTime = maxBarkTime    # (2)
        self.__name = name

    def __isReachedMaxBarkTime(self):       # (3)
        return self.__timeBarked >= self.__maxBarkTime

    def bark(self):
        if self.__isReachedMaxBarkTime():   # (4)
            return '...'
        else:
            self.__timeBarked += 1
            return f'{self.__name} woof woof'

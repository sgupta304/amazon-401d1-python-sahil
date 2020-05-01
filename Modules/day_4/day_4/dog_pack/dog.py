from abc import ABC, abstractmethod


class Dog(ABC):
    count = 0

    def __init__(self, name="Unknown"):
        self.name = name
        self.__private_var = "private_var"
        Dog.count += 1
        # self.__class__.count += 1

    @abstractmethod
    def greet(self):
        return None

    @staticmethod
    def sleep():
        return "zzz"

    @classmethod
    def get_dog_count(cls):
        return f"The number of dogs created is {cls.count}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. name: {self.name}"

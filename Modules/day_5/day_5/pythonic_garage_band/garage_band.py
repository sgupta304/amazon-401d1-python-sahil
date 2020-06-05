from abc import ABC, abstractmethod


class Band:
    instances = []

    def __init__(self, name, members=None):
        if members is None:
            members = []
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band with instance with name={self.name}, with members={self.members}"

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        return [member.play_solo() for member in self.members]


class Musician(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Musician with name {self.name}"

    def __repr__(self):
        return f"Musician with instance with name={self.name}, with instance={self.__class__.__name__}"

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bassist solo"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "drummer solo"

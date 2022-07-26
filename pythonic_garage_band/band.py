class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def __str__(self):
        return f"We are {self.name}, with members {self.members}."

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def play_solos(self):
        solos = []
        for x in self.members:
            solos.append(x.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return self.__class__.instrument

    def play_solo(self):
        return self.__class__.solo

class Guitarist(Musician):
    instrument = "guitar"
    solo = "face melting guitar solo"

class Bassist(Musician):
    instrument = "bass"
    solo = "bom bom buh bom"

class Drummer(Musician):
    instrument = "drums"
    solo = "rattle boom crash"
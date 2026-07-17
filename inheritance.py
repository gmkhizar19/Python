class PartyAnimal:
    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print("Self.name construscted")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


class FootbalFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal("sally")
s.party()

j = FootbalFan("jim")
j.party()
j.touchdown()

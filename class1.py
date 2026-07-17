class Partyanimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = Partyanimal()

an.party()
an.party()
an.party()


print("type", type(an))
print("dir: ", dir(an))
print("type: ", type(an.x))
print("type: ", type(an.party))

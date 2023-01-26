from . import Human
from . import Pet


class HumanWithPet(Human):

    def __init__(self, first_name, last_name, pets=[]):
        super().__init__(first_name, last_name)
        self.pets = pets

    def __str__(self):
        pass


    def adopt_new_pet(self, pets):
        print(self.pets)
        while True:

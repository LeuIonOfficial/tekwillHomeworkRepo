from lesson_19_homework.Human import Human


class Pet:

    def __init__(self, pet_name: str, pet_species: str, pet_favourite_food: str):
        self.pet_name = pet_name
        self.pet_species = pet_species
        self.pet_favourite_food = pet_favourite_food

    def __str__(self):
        pass

    def get_pet_name(self):
        return self.pet_name

    def get_pet_species(self):
        return self.pet_species

    def get_pet_favourite_food(self):
        return self.pet_favourite_food


class HumanWithPet(Human):

    def __init__(self, first_name, last_name, pets):
        super().__init__(first_name, last_name)
        self.pets = pets

    def __str__(self):
        pass

    def adopt_new_pet(self):
        self.pets = [Pet.get_pet_name(), Pet.get_pet_species()]
        return self.pets


kuzea = Pet("Kuzea", "dog", "macaroons")
print(f'{Pet.get_pet_species(kuzea).capitalize()} called '
      f'{Pet.get_pet_name(kuzea).capitalize()} '
      f'that loves {Pet.get_pet_favourite_food(kuzea)}')

valera = HumanWithPet("Ion", "Leu")
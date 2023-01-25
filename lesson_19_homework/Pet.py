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


kuzea = Pet("Kuzea", "dog", "macaroons")
print(f'{Pet.get_pet_species(kuzea).capitalize()} called '
      f'{Pet.get_pet_name(kuzea).capitalize()} '
      f'that loves {Pet.get_pet_favourite_food(kuzea)}')

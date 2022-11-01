
import unittest
from animal import Animal

class Test_animal(unittest.TestCase):
    def test_animal_cat(self):
        animal1 = Animal
        if animal1.type == "cat":
            self.assertEqual(animal1.name, "Seymour")

    def test_animal_dog(self):
        animal1 = Animal
        if animal1.type == "dog":
            self.assertEqual(animal1.name, "Spot")   

    def test_animal_name(self):
        animal1 = Animal
        if animal1.name == self.name:
            self.assertEqual(animal1.name, self.name)

    def test_animal_speakC(self):
        animal1 = Animal
        if animal1.type == "cat" and animal1.size == "small":
            self.speak("meow")
        else:
            self.speak("MEOW")

    def test_animal_speakD(self):
        animal1 = Animal
        if animal1.type == "dog" and animal1.size == "small":
            self.speak("bow wow")
        elif animal1.type == "dog" and animal1.size == "medium":
            self.speak("Ruff ruff") 
        else:
            self.speak("arf arf")

    def test_animal_age(self):
        animal1 = Animal
        if animal1.age < 10:
            self.describe(self.name, "is young.")
        else:
            self.describe(self.name, "is old.")




    
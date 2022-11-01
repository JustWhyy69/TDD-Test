
import unittest
from animal import Animal

class Test_animal(unittest.TestCase):
    def test_animal_cat(self):
        animal1 = Animal("cat")
        self.assertEqual(animal1.name, "Seymour")

    def test_animal_dog(self):
        animal1 = Animal("dog")
        self.assertEqual(animal1.name, "Spot")   

    def test_animal_name(self):
        animal1 = Animal()
        self.assertEqual(animal1.name, self.name)

    def test_animal_speakC(self):
        cat1 = Animal("cat")
        cat1.size= "small"
        words1 = cat1.speak
        self.assertEqual(words1, "meow")

        cat2 = Animal("cat")
        cat2.size= "medium"
        words2 = cat2.speak
        self.assertEqual(words2, "MEOW")


    def test_animal_speakD(self):
        dog1 = Animal("dog")
        dog1.size= "small"
        words1 = dog1.speak
        self.assertEqual(words1, "bow wow")

        dog2 = Animal("dog")
        dog2.size= "medium"
        words2 = dog2.speak
        self.assertEqual(words2, "Ruff ruff")
        
        dog3 = Animal("dog")
        dog3.size= "large"
        words3 = dog3.speak
        self.assertEqual(words3, "arf arf")

  

    def test_animal_age(self):
        animal1 = Animal()
        animal1.size = < 10
        self.describe(self.name, "is young")

        animal1 = Animal()
        animal1.size = > 10
        self.describe(self.name, "is old")




    
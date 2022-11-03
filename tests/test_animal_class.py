import unittest
from animal import Animal

class Test_animal(unittest.TestCase):

    def test_default_name_cat(self):
        cat = Animal("cat")
        pass
        self.assertEqual(cat.name, "Seymour")

    def test_default_name_dog(self):
        dog = Animal("dog")
        pass
        self.assertEqual(dog.name, "Spot")

    def test_provided_name(self):
        assigned_name = "Killer"
        dog = Animal("dog")
        dog.name = assigned_name
        pass
        self.assertEqual(dog.name, assigned_name)

    def test_cat_speak(self):
        cat1 = Animal("cat")
        cat1.size = "small"
        words1 = cat1.speak()
        self.assertEqual(words1, "meow")

        cat2 = Animal("cat")
        cat2.size = "medium"
        words2 = cat2.speak()
        self.assertEqual(words2, "MEOW!")

    def test_dog_speak(self):
        dog1 = Animal("dog")
        dog1.size = "small"
        words1 = dog1.speak()
        self.assertEqual(words1, "bow wow")

        dog2 = Animal("dog")
        dog2.size = "medium"
        words2 = dog2.speak()
        self.assertEqual(words2, "Ruff ruff")

        dog3 = Animal("dog")
        dog3.size = "notsmallormedium"
        words3 = dog3.speak()
        self.assertEqual(words3, "arf arf")

    def test_age(self):
        dog1 = Animal("dog")
        dog1.age = 9
        desc1 = dog1.describe()
        self.assertEqual(desc1, f"{dog1.name} is young")

        dog2 = Animal("dog")
        dog2.age = 10
        desc2 = dog2.describe()
        self.assertEqual(desc2, f"{dog2.name} is old")


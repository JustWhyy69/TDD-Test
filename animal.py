class Animal(): 
    def __init__(self, ctype):
        self.name = ""
        self.size = ""
        self.type = ctype
        self.age = 0    

        if self.type == "cat":
            self.name = "Seymour"
        elif self.type == "dog":
            self.name = "Spot"



    def speak(self):
        if self.type == "cat":
            if self.size == "small":
                return "meow"
            elif self.size == "medium":
                return "MEOW!"

        elif self.type == "dog":
            if self.size == "small":
                return "bow wow"
            elif self.size == "medium":
                return "Ruff ruff"
            elif self.size == "notsmallormedium":
                return "arf arf"

    def describe(self):
        if self.age < 10:
            return f"{self.name} is young"
        elif self.age > 9:
            return f"{self.name} is old"


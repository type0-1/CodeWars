from preloaded import Animal

class Cat(Animal):
    
    def __init__(self, animal):
        self.animal = animal
    
    def speak(self):
        return f'{self.animal} meows.'
    

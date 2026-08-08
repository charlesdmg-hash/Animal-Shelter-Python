class Animal:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def make_sound(self):
        print("The animal makes a sound")

    def feed(self):
        print("The animal eats")

    def sleep(self):
        print("The animal sleeps")

class Dog(Animal):
    def __init__(self, name: str, type: str,  breed: str):
        super().__init__(name, type)
        self.breed = breed

    def make_sound(self):
            print("The dog says WOOF WOOF")
    
    def feed(self):
            print("The dog eats the bone")
    
    def sleep(self):
            print("The dog sleeps inside")

class Cat(Animal):
    def __init__(self, name: str, type: str,  breed: str):
        super().__init__(name, type)
        self.breed = breed

    def make_sound(self):
            print("The cat says Miau")
    
    def feed(self):
            print("The cat eats the fish")
    
    def sleep(self):
            print("The cat sleeps inside")

class Bird(Animal):
    def __init__(self, name: str, type: str,  specie: str):
        super().__init__(name, type)
        self.specie = specie

    def make_sound(self):
            print("The bird chirps")
    
    def feed(self):
            print("The bird eats the rat")
    
    def sleep(self):
            print("The bird sleeps outside")



animal = Animal("Doggy", "Dog")
dog = Dog("wow wow", "Dog", "Labrador")
cat = Cat("Garfield", "Cat", "Angola")
bird = Bird("sussy", "Bird", "Falcon")

animal.feed()
animal.make_sound()
animal.sleep()

print()

dog.feed()
dog.make_sound()
dog.sleep()

print()

cat.feed()
cat.make_sound()
cat.sleep()

print()

bird.feed()
bird.make_sound()
bird.sleep()



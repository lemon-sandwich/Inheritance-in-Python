class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.") # The reason we write f is: It get's the things in the flower bracket and replace them
                                                                  # with their respective var

    def speak(self):
        print(" :( ")


class Cat(Pet): # We can use the Pet function in this class and same functions will get overwriten
    def __init__(self,name,age,color):
        self.color = color
        super().__init__(name,age) # Name and age are already defined in the Pet's constructor. To bring it here, we just need to pass this
    
    def speak(self):
        print("Meow")

class Fish(Pet):
    pass

class Dog(Pet):
    
    def speak(self):
        print("Bark")
c = Cat("Skittles", 2, "White")
c.show()
c.speak()
d = Dog("Craig",4)
d.show()
d.speak()
f = Fish("SquidWard",1)
f.show()
f.speak()

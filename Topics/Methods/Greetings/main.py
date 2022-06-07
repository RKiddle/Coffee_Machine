class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f"Hello, I am {self.name}!")
        
input_name = input()
bob = Person(input_name)
bob.greet()

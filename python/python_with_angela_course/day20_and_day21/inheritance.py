# Class inheritance is the concept of inheriting behavior and appearance features
# from an existing class

# Inheriting behavior from an existing class is inheriting methods from an existing class
# Whereas, inheriting appearance from an existing class is inheriting attributes from an existing class

# Example below:

class Animal:

    def __init__(self):
        self.num_eyes = 2
        self.fur = True
    
    def number_of_eyes(self):
        print(f"An animal has {2} eyes.")

class Lion(Animal):

    def __init__(self):
        super().__init__()
        self.tail = 'do'

    def number_of_eyes(self):
        super().number_of_eyes()
        print('This fact includes lions.')
    
    def body_parts(self):
        print(f"It is {self.fur} that lions have fur. Lastly, lions {self.tail} have tails.")

simba = Lion()

simba.number_of_eyes()
simba.body_parts()
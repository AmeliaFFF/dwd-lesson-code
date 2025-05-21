class Dog:
    def __init__(self, name_param, breed_param, age_param):
        print(f"A new dog named {name_param} is being created!")
        self.name = name_param  # Instance variable
        self.breed = breed_param # Instance variable
        self.age = int(age_param)

    # This is a method
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}.")
        
    def get_age(self):
        print(f"{self.name} is {self.age} years old.")
    
    def celebrate_birthday(self):
        self.age += 1
        return self.age

# Create an object (instance) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 5)

# Call methods on the objects
dog1.describe()
dog1.bark()
dog1.get_age()
new_age = dog1.celebrate_birthday()

print("-" * 10) # Separator

print(f"Dog 1's name is: {dog1.name}")
print(f"Dog 1's breed is: {dog1.breed}")
print(f"Dog 1's age is: {dog1.age - 1}")
print(f"Dog 1's new age is: {new_age}")
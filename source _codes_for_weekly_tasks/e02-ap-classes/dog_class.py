class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age, gender, breed=None):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def give_paw(self):
        """Simulate a dog giving its paw in response to a command."""
        print(f"{self.name} is giving its paw now!")

    def bark(self, number_of_barks=1):
        """Simulate a dog barking one or more times in response to a command"""
        barking_sound = "Woof! "
        print(f"{barking_sound * number_of_barks}")


my_dog = Dog("Pasa", 12, "Male", "Golden Retriever")
my_sisters_dog = Dog("Odin", 2, "Male", "German Shephard")
print(f"I have a {my_dog.age} year-old {my_dog.gender} {my_dog.breed} and his name is {my_dog.name.title()}.")
print(f"My sister Hazal has a {my_sisters_dog.age} year-old {my_sisters_dog.gender} {my_sisters_dog.breed} and his name is {my_sisters_dog.name.title()}.")

my_dog.sit()
my_dog.roll_over()
my_dog.bark()
my_sisters_dog.give_paw()
my_sisters_dog.bark(3)

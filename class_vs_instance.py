# Write a Person class with an instance variable,age , and a constructor that takes an integer,initialAge , as a parameter. 
# The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; 
# if a negative argument is passed as initialAge, the constructor should set age to 0 and print Age is not valid, setting age to 0.. 
# In addition, you must write the following instance methods:
# yearPasses() should increase the  instance variable by .
# amIOld() should perform the following conditional actions:
# If age < 13, print You are young..
# If 13 < age < 18 and , print You are a teenager..
# Otherwise, print You are old..
# To help you learn by example and complete this challenge, much of the code is provided for you, 
# but you'll be writing everything in the future. 
# The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!
# Note: Do not remove or alter the stub code in the editor.
# Input Format
# Input is handled for you by the stub code in the editor.
# The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        elif initialAge >= 100:
            self.age = initialAge
        else:
            self.age = initialAge
        return None
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
        return None

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        return None


t = int(input())

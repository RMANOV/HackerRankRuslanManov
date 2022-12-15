# Objective
# Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video.

# Task
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# A Student class constructor, which has  parameters:
# A string, .
# A string, .
# An integer, .
# An integer array (or vector) of test scores, .
# A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg < 40:
            return "T"
        elif avg < 55:
            return "D"
        elif avg < 70:
            return "P"
        elif avg < 80:
            return "A"
        elif avg < 90:
            return "E"
        else:
            return "O"


line = input().split()

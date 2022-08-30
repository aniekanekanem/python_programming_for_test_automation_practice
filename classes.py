import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        # initialize attributes to be used in/available for all
        # class methods in this class, and for class objects created by this class.

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        # all people introduce themselves
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emotion(self):
        # emotions of each person described, if statment used
        # here depending on the person
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        # totally healthy >=97, unwell >=80, see doctor <=79
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 80:
            print("{} feels unwell".format(self.firstname))
        else:
            print("{} goes to the Doctor".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 100, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.emotion()
Rey.emotion()
Lee.emotion()

Maria.status_change()
Rey.status_change()
Lee.status_change()

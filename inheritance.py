import classes

# creating an enemy class and assigning methods to it


class Enemy(classes.Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    # hurt method
    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    # insult method
    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    # steal method
    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.hurt(classes.Maria)
Alex.insult(classes.Rey)
Alex.insult(classes.Lee)
Alex.steal(classes.Rey)

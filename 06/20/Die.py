from random import randint

class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        result = randint(1,6)
        print(result)

    def six(self):
        for i in range(10):
            result = randint(0, 6)
            print(result)

    def ten(self):
        for i in range(10):
            result = randint(0,10)
            print(result)
    def tew(self):
        for i in range(20):
            result = randint(0,20)
            print(result)


d = Die();
#d.six()
#d.ten()
d.tew()




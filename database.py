#Data base file
#So far the script can only read from this file and not update it. That will have to change...

class person ():
    def __init__(self):
        self.name = ""
        self.id = 0
        self.money = 0
        self.netWorth = 0
        self.salary = 0
        self.income = 0
        self.expenses = 0
        self.netIncome = 0

#james stats
james = person
james.name = "james"
james.id = 2
james.money = 1234
james.netWorth = 4321
james.netIncome = 23532
james.expenses = 32
james.income = 352
james.salary = 200000

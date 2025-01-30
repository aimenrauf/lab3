class Expenses:
    def __init__(self):
        self.expense = []
    def addExpenses(self,amount):
        self.expense.append(amount)
    def calculateExpense(self):
        return sum(self.expense[:7])
        
exp = Expenses()
exp.addExpenses(100)
exp.addExpenses(200)
exp.addExpenses(499)
exp.addExpenses(3432)
exp.addExpenses(788)
exp.addExpenses(233)
exp.addExpenses(97)
exp.addExpenses(987)
totalamount = exp.calculateExpense()
print(f"Expenses for the first 7 days are {totalamount}")
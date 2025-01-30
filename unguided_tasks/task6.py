class Expenses:
    def __init__(self):
        self.category = ["EatOut","Fuel","Party"]
        self.expenses = [[] for _ in range(len(self.category))]
    def addExpenses(self, category, amount):
        if 0 <= category < len(self.category):
            self.expenses[category].append(amount)
        else:
            print("Invalid data Entry")
    def calculateTotal (self):
        total = []
        for expenses in self.expenses:
            total.append(sum(expenses))
            print(f"Total Expenses: {total}")
    def display(self):
        print("Expenses in Category:")
        for i,category in enumerate (self.category):
            totala = sum(self.expenses[i])
            print(f"{category}: {totala} (Details: {self.expenses[i]})")
track = Expenses()
track.addExpenses(0,34)
track.addExpenses(1,100)
track.addExpenses(2,988)
track.addExpenses(1,10000)
track.addExpenses(0,765)
track.display()
track.calculateTotal()


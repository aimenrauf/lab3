class List:
    def __init__(self):
        self.numbers = []
    def addNumber(self,number):
        self.numbers.append(number)
    def maximum(self):
        max = 0
        for i,number in enumerate(self.numbers,1):
            if number>max:
                max = number
        return max
ls = List()
for i in range(6):
    num = input(f"Enter the num {i+1}: ")
    ls.addNumber(int(num))
print(f"Maximum number in the list is: {ls.maximum()}")
class Grade:
    def __init__(self):
        self.marks = [56, 87, 45, 98, 67]
        self.grade = []
    def calculateAverage(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        return average
    def calculateGrade(self, average):
        for index, mark in enumerate(self.marks, 1):
            if mark > average:
                self.grade.append("A")
            elif mark == average:
                self.grade.append("A-")
            else:
                self.grade.append("B+")
    def viewGrade(self):
        for i, grade in enumerate(self.grade, 1):
            print(f"{i}. {grade}")
grading = Grade()
average = grading.calculateAverage()
grading.calculateGrade(average)
grading.viewGrade()
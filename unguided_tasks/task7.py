class Tracker:
    def __init__(self):
        self.employee = ["Ali", "Ahmed", "Junaid","Usama","Rashid"]
        self.attendence = [[] for _ in range (len(self.employee))]
    def attend(self,emp,attendence):
        if 0<=emp < len(self.attendence):
            self.attendence[emp].append(attendence)
        else:
            print("Invalid employee number")
    def calculateAttendence(self):
        for emp_in,emp in enumerate(self.employee):
            total =0
            for attendence in self.attendence[emp_in]:
                if attendence == 1:
                    total = total + 1
            average =total/5
            print(f"{emp_in + 1}) {emp}: {total} (Details: {self.attendence[emp_in]})")
            print(f"Average: {average}")
track = Tracker()
track.attend(0,1)
track.attend(1,1)
track.attend(2,1)   
track.attend(3,1)
track.attend(4,1)
track.attend(0,0)
track.attend(1,1)
track.attend(2,1)   
track.attend(3,0)
track.attend(4,1)
track.attend(0,1)
track.attend(1,1)
track.attend(2,0)   
track.attend(3,1)
track.attend(4,0)
track.attend(0,1)
track.attend(1,1)
track.attend(2,0)   
track.attend(3,1)
track.attend(4,1)
track.attend(0,0)
track.attend(1,1)
track.attend(2,0)   
track.attend(3,1)
track.attend(4,1)
track.calculateAttendence()


        
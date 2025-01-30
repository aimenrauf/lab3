class ToDoList:
    def __init__(self):
        self.tasks = []
        self.checked_task = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found.")
    def view_tasks(self):
        print("tasks: ")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("Checked_tasks: ")
        for i,task in enumerate(self.checked_task,1):
            print(f"{i}. {task}")
    def check_task(self,task):
        if task in self.tasks:
            print(f"Task '{task}' is completed.")
            self.checked_task.append(task) 
to_do = ToDoList()
to_do.add_task("Buy groceries")
to_do.add_task("Complete homework")
to_do.view_tasks()
to_do.check_task("Buy groceries")
to_do.view_tasks()
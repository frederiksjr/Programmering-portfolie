class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    def work(self):
        print(f"{self.name} is working as a {self.position}.")

    def report_salary(self):
        print(f"{self.name}'s salary is {self._salary}.")


class Manager(Employee):
    def __init__(self, name, salary, team=None):
        super().__init__(name, "Manager", salary)
        self.team = team

    def assign_task(self, employee, task):
        employee.work_on_task(task)

    def work_on_task(self, task):
        print(f"{self.name} is working on {task}.")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, "Developer", salary)
        self.programming_language = programming_language

    def work_on_task(self, task):
        print(f"{self.name} is working on {task} using {self.programming_language}.")


manager = Manager("John Doe", 80000)
developer = Developer("Jane Smith", 60000, "Python")

manager.assign_task(developer)

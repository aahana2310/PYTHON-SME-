class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._attendance = 0

    # Get and set methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Get and set methods for salary
    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    # Get and set methods for attendance
    def get_attendance(self):
        return self._attendance

    def set_attendance(self, days):
        self._attendance = days

    # Mark attendance (adds 1 day)
    def mark_attendance(self):
        self._attendance += 1

    # Display employee details
    def display(self):
        print("Employee Name :", self._name)
        print("Salary        :", self._salary)
        print("Attendance    :", self._attendance, "day(s)")

# Example usage
emp = Employee("AAHANA", 125000)
emp.mark_attendance()
emp.mark_attendance()
emp.display()

emp.set_name("AAHANA CHOMTU")
emp.set_salary(150000)
emp.display()

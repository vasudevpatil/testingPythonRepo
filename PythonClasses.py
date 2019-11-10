import datetime


class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        # return super().__repr__()
        # return "Employee ('{ }' , '{ }')".format(self.first, self.last)
        return " { } - { }".format(self.fullname, self.email)


"""
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang, *args, **kwargs):
        super().__init__(first, last, pay, *args, **kwargs)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None, *args, **kwargs):
        super().__init__(first, last, pay, *args, **kwargs)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())

"""
emp1 = Employee("Vasudev", "Patil", 50000)
emp2 = Employee("test", "user", 60000)

print(emp1)
# repr(emp1)
# str(emp1)

"""
dev_1 = Developer("Vasudev", "Patil", 50000, "Python")
dev_2 = Developer("test", "user", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.rem_emp(dev_1)
mgr_1.print_emp()

# print(dev_2.email)
# print(dev_2.prog_lang)

# print(help(Developer))


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


emp1 = Employee("Vasudev", "Patil", 50000)
emp2 = Employee("test", "user", 60000)
Employee.set_raise_amt(1.05)


my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

print(emp1.fullname())
print(Employee.num_of_employees)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
"""

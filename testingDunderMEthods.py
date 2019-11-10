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

    def __repr__(self):
        return "Employee( '{}', '{}', {} )".format(self.first, self.last, self.pay)


#    def __str__(self):
#        return "{} - {}".format(self.fullname, self.email)


emp1 = Employee("Vasudev", "Patil", 50000)
emp2 = Employee("test", "user", 60000)

print(emp1)

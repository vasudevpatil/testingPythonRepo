class Employee:
    def __init__(self, first, last, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first = first
        self.last = last
        # self.pay = pay
        # self.email = first + "." + last + "@company.com"
        # Employee.num_of_employees += 1

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp1 = Employee("Vasudev", "Patil")
emp2 = Employee("test", "user")

emp1.fullname = "John Smith"
# emp1.first = "Jim"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

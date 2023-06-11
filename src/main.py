class Laptop:
    def __init__(self, brand):
        self.brand = brand
        self.age = 10

    def add_year(self, increment):
        self.age = self.age + increment


my_lapo = Laptop('Lenovo')
my_lapo.add_year(5)
print(my_lapo.age)
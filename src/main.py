class Phone:
    def __init__(self, brand):
        self.brand = brand
    
my_phone = Phone('SAMSUNG')
grandma_phone = Phone('NOKIA 1100')
print(my_phone.brand)
print(grandma_phone.brand)
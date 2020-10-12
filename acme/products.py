class Product:
    def __init__(self, name, code, price):
        self.name = name 
        self.code = code 
        self.price = price 


    def get_name(self):
        return self.name 

    def get_code(self):
        return self.code 

    def get_price(self):
        return self.price 

    def update_price(self, value):
        self.price = value 

    def __repr__(self):
        return f"Widget: {self.name}, {self.code}, {self.price}"
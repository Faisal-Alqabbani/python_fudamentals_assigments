class Store:
    def __init__(self,name):
        self.name = name
        self.list = []
    def add_product(self, newProduct):
        self.list.append(newProduct)
        return self
    def sell_product(self, id):
        self.list.remove(id)
        return self
    def inflation(self, percent_increase):
        for i in range(len(self.list):
            i.price += (percent_increase * i.price)
        return self
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.list)):
            if self.list[i].category == category:
                udpate_price(percent_change=percent_discount, is_increased=False)
        
    
class Product:
    def __init__(self, name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def udpate_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (percent_change * self.price)
        else:
            self.price -= (percent_change * self.price)
    def print_info(self):
        print(f"Product name is {self.name} prodcut price is {self.price} and prodcut category is {self.category}")

            
    
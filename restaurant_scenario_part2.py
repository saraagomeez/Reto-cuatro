class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price 
    
    def set_price(self, price):
        self._price = price
    
    def calculate_total_price(self):
        return self.price
    
class Appetizers(MenuItem):
    def __init__(self, name:str, price:int, servings:int):
        super().__init__(name, price)
        self._servings = servings

    def get_servings(self):
        return self._servings
    
    def set_servings(self, servings):
        self._servings = servings

class Soups(MenuItem):
    def __init__(self, name:str, price:int, type:str):
        super().__init__(name, price)
        self.type = type #cream or soup

    def get_type(self):
        return self._type
    
    def set_type(self, type):
        self._type = type

class Salads(MenuItem):
    def __init__(self, name:str, price:int, dressing:bool):
        super().__init__(name, price)
        self.dressing = dressing

    def get_dressing(self):
        return self._dressing
    
    def set_dressing(self, dressing):
        self._dressing = dressing

class MainCourse(MenuItem):
    def __init__(self, name:str, price:int, portion_size:int):
        super().__init__(name, price)
        self.portion_size = portion_size

    def get_portion_size(self):
        return self._portion_size
    
    def set_portion_size(self, portion_size):
        self._portion_size = portion_size

class Desserts(MenuItem):
    def __init__(self, name:str, price:int, flavor:str):
        super().__init__(name, price)
        self.flavor = flavor

    def get_portion_flavor(self):
        return self._flavor
    
    def set_flavor(self, flavor):
        self._flavor = flavor

class Beverages(MenuItem):
    def __init__(self, name:str, price:int, alcoholic:bool):
        super().__init__(name, price)
        self.alcoholic = alcoholic

    def get_alcoholic(self):
        return self._alcoholic
    
    def set_alcoholic(self, alcoholic):
        self._alcoholic = alcoholic

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.calculate_total_price() for item in self.items)
        return total
    
menu_items = [
    Appetizers("Carpaccio", 25000, 1),
    Appetizers("Shrimps", 35000, 1),
    Appetizers("Cheese plate", 30000, 3),
    Soups("Onion soup", 25000, "soup"),
    Soups("Tomato soup", 30000, "Cream"),
    Soups("Mushrooms soup", 25000, "Cream"),
    Salads("Cesar salad", 20000, True),
    Salads("Smoked salmon salad", 35000, False),
    Salads("Caprese salad", 25000, True),
    MainCourse("steak with wine sauce", 60000, "Medium"),
    MainCourse("Seafood risotto", 50000, "Big"),
    MainCourse("Duck in red fruits", 65000, "Small"),
    Desserts("Chocolate cake", 25000, "Chocolate"),
    Desserts("Creme brulee", 20000, "Milk"),
    Desserts("Souffle", 30000, "Red fruits"),
    Beverages("Water", 8000, False),
    Beverages("Soda", 12000, False),
    Beverages("Bottle of wine", 120000, True),
    Beverages("Bottle of champagne", 250000, True)
    ]
    
order = Order()
order.add_item(menu_items[1])
order.add_item(menu_items[4])
order.add_item(menu_items[7])
order.add_item(menu_items[11])
order.add_item(menu_items[14])
order.add_item(menu_items[15])
order.add_item(menu_items[18])

print ("Order: ")
for item in order.items:
    print("\n",(item.name, item.price))
print("\nTotal bill: ", order.calculate_total(), "COP\n")
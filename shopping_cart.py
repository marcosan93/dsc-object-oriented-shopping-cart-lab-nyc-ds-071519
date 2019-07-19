class ShoppingCart:
    
    # write your code here
    def __init__(self, emp_discount=None, total=0, items = []):
        self.employee_discount = emp_discount
        self.total = total
        self.items = []

    
    def add_item(self, name, price, quantity=1):
        self.total = self.total + price*quantity
        for i in range(quantity):
            self.items.append([name, price])
        return self.total
    
    def mean_item_price(self):
        return round(self.total/len(self.items), 2)

    def median_item_price(self):
        #figuring out median, list of multiple dictionaries were printed out, trying to get just one dictionary
    
        #print(self.items)
        sorted_items = sorted([i[-1] for i in self.items])
        #print(sorted_items)
        
        if len(sorted_items) % 2 != 0:
            return sorted_items[int(len(sorted_items)/2+1)]
        else:
            return sum(sorted_items[int(len(sorted_items)/2+1)]+sorted_items[int(len(sorted_items)/2)])/2
    def apply_discount(self):
        discount = self.employee_discount
        if isinstance(discount, int):
            return self.total*(1-(discount/100))
        else:      
            return "Sorry, there is no discount to apply to your cart :("


    def void_last_item(self):
        if len(self.items) > 0:
            print(self.total, self.items[-1][-1])
            self.total = self.total - self.items[-1][-1]
            del self.items[-1]
            return self.total
        else:
            return "There are no items in your cart!"
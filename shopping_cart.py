class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
      self.total = 0
      self.employee_discount = emp_discount
      self.items = []
    def add_item(self, name, price, quantity=1):
       self.items.append([name, price, quantity])
       self.total += price * quantity if quantity > 0 else price
       return f'New cart total is ${self.total}.'
    def mean_item_price(self):
        prices = []
        for n, p, q in self.items:
            count = q
            while count >= 1:
                count -= 1
                prices.append(p)
        return round((sum(prices)/len(prices)) - .005, 2)
        
    def median_item_price(self):
        prices = []
        for n, p, q in self.items:
            count = q
            while count >= 1:
                count -= 1
                prices.append(p)
        if len(prices)%2==1:
            return sorted(prices)[(len(prices)//2)]
        else:
            return round((sorted(prices)[len(prices)//2] +
                   sorted(prices)[(len(prices)//2) + 1]) / 2, 2)

    def apply_discount(self):
        if self.employee_discount:
            return f'''Discounted total is ${round(self.total * ((100 - self.employee_discount) / 100), 2)}.'''
        return 'Sorry, there is no discount to apply to your cart. :('

    def void_last_item(self):
        if len(self.items) >= 1:
            if self.items[-1][2] > 1:
                self.items[-1][2] -= 1
                self.total -= self.items[-1][1]
            else:
                self.total -= self.items[-1][1]
                self.items.remove[-1]
        else:
            return "There are no items in your cart!"
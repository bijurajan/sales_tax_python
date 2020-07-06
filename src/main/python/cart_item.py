class CartItem:
    def __init__(self, item, price):
        self.price = price
        self.item = item

    def calculate_price(self):
        return self.price



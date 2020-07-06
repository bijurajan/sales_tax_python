class CartItem:
    def __init__(self, item, price):
        self.price = price
        self.item = item

    def calculate_price(self):
        if self.item.is_exempt:
            return "0.00"
        return f'{(self.price * 10) / 100 :0.2f}'



import math


class CartItem:
    def __init__(self, item, price):
        self.price = price
        self.item = item

    def calculate_price(self):
        if self.item.is_exempt and self.item.is_imported:
            return f'{self.price * 5 / 100:0.2f}'
        if self.item.is_exempt:
            return "0.00"
        if self.item.is_imported:
            basic_sales_tax = self.round_up_to_2_decimals(self.price * 10/100)
            import_tax = self.round_up_to_2_decimals(self.price * 5/100)
            return f'{(basic_sales_tax + import_tax):0.2f}'
        return f'{(self.price * 10) / 100 :0.2f}'

    def round_up_to_2_decimals(self, price):
        return math.ceil(price * 20) / 20





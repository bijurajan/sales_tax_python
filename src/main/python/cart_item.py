import math


class CartItem:
    def __init__(self, item, price):
        self.price = price
        self.item = item

    def calculate_sales_tax(self):
        sales_tax = self.calculate_sales_tax_value()
        return f'{sales_tax:0.2f}'

    def calculate_sales_tax_value(self):
        if self.item.is_exempt and self.item.is_imported:
            return self.price * 5 / 100
        if self.item.is_exempt:
            return 0
        if self.item.is_imported:
            basic_sales_tax = self.round_up_to_2_decimals(self.price * 10/100)
            import_tax = self.round_up_to_2_decimals(self.price * 5/100)
            return basic_sales_tax + import_tax
        return self.price * 10 / 100

    def calculate_price_with_tax(self):
        return f'{(self.price + self.calculate_sales_tax_value()):0.2f}'

    def round_up_to_2_decimals(self, price):
        return math.ceil(price * 20) / 20



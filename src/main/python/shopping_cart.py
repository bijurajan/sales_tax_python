from functools import reduce


class ShoppingCart:

    def __init__(self, cart_items):
        self.cart_items = cart_items

    def calculate_sales_tax(self):
        sales_tax_values = list(map(lambda cart_item: float(cart_item.calculate_sales_tax()), self.cart_items))
        sales_tax = reduce(lambda tax1, tax2: tax1 + tax2, sales_tax_values)
        return f'{sales_tax:0.2f}'

    def calculate_total(self):
        price_values = list(map(lambda cart_item: float(cart_item.calculate_price_with_tax()), self.cart_items))
        total_price = reduce(lambda tax1, tax2: tax1 + tax2, price_values)
        return f'{total_price:0.2f}'

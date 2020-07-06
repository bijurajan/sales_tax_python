from cart_item import CartItem

from item import Item


class TestCartItem:
    def test_should_not_add_sales_tax_on_exempt_items(self):
        item = Item(True, False)
        price = 12.49
        result = CartItem(item, price).calculate_price()
        assert result == "0.00"

    def test_should_add_sales_tax_on_non_exempt_items(self):
        item = Item(False, False)
        price = 14.99
        result = CartItem(item, price).calculate_price()
        assert result == "1.50"

    def test_should_add_import_duty_only_on_exempt_items(self):
        item = Item(True, True)
        price = 10.00
        result = CartItem(item, price).calculate_price()
        assert result == "0.50"

    def test_should_add_sales_tax_and_import_duty_on_non_exempt_items(self):
        item = Item(False, True)
        price = 47.50
        result = CartItem(item, price).calculate_price()
        assert result == "7.15"

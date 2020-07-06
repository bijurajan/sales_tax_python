from cart_item import CartItem
from item import Item


class TestCartItem:
    def test_should_not_add_sales_tax_on_exempt_items(self):
        item = Item(True, False)
        price = 12.49
        result = CartItem(item, price).calculate_price()
        assert result == 12.49

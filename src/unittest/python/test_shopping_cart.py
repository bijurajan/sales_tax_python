from cart_item import CartItem
from item import Item
from shopping_cart import ShoppingCart


class TestShoppingCart:

    """
        Input 1:
            1 book at 12.49
            1 music CD at 14.99
            1 chocolate bar at 0.85

         Output 1:
            1 book : 12.49
            1 music CD: 16.49
            1 chocolate bar: 0.85
            Sales Taxes: 1.50
            Total: 29.83
    """
    def test_validate_input_1(self):
        cart_items = list([
            CartItem(Item(True, False), 12.49),
            CartItem(Item(False, False), 14.99),
            CartItem(Item(True, False), 0.85),
        ])
        shopping_cart = ShoppingCart(cart_items)

        assert shopping_cart.calculate_sales_tax() == "1.50"
        assert shopping_cart.calculate_total() == "29.83"

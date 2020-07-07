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

    """
        Input 2:
            1 imported box of chocolates at 10.00
            1 imported bottle of perfume at 47.50
        Output 2:
            1 imported box of chocolates: 10.50
            1 imported bottle of perfume: 54.65
            Sales Taxes: 7.65
            Total: 65.15
    """
    def test_validate_input_2(self):
        cart_items = list([
            CartItem(Item(True, True), 10.00),
            CartItem(Item(False, True), 47.50),
        ])
        shopping_cart = ShoppingCart(cart_items)

        assert shopping_cart.calculate_sales_tax() == "7.65"
        assert shopping_cart.calculate_total() == "65.15"

    """
        Input 3:
            1 imported bottle of perfume at 27.99
            1 bottle of perfume at 18.99
            1 packet of headache pills at 9.75
            1 box of imported chocolates at 11.25
        Output 3:
            1 imported bottle of perfume: 32.19
            1 bottle of perfume: 20.89
            1 packet of headache pills: 9.75
            1 imported box of chocolates: 11.85
            Sales Taxes: 6.70
            Total: 74.68
    """
    def test_validate_input_3(self):
        cart_items = list([
            CartItem(Item(False, True), 27.99),
            CartItem(Item(False, False), 18.99),
            CartItem(Item(True, False), 9.75),
            CartItem(Item(True, True), 11.25)
        ])
        shopping_cart = ShoppingCart(cart_items)

        assert shopping_cart.calculate_sales_tax() == "6.70"
        assert shopping_cart.calculate_total() == "74.68"

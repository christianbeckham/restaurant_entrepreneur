from order import Order


class Pizza(Order):
    '''A class to represent a pizza order.

    This class inherits from Order.

    Attributes:
        dish_name: A string to represent the name of the dish.
        price: An integer to represent the price of a dish.
    '''

    def __init__(self):
        super().__init__()
        self.dish_name = 'Pizza'
        self.price = 15

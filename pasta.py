from order import Order


class Pasta(Order):
    '''A class to represent a pasta order.

    This class inherits from Order.

    Attributes:
        dish_name: A string to represent the name of the dish.
        price: An integer to represent the price of a dish.
    '''

    def __init__(self):
        super().__init__()
        self.dish_name = 'Pasta'
        self.price = 10

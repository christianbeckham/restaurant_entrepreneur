class Order:
    '''A class to represent an Order.

    This is a blueprint for child classes to inherit from.

    Attributes:
        dish_name: A string to represent the name of the dish.
        price: An integer to represent the price of a dish.
    '''

    def __init__(self):
        self.dish_name = ''
        self.price = 0

from order import Order


class Pizza(Order):
    def __init__(self):
        super().__init__()
        self.dish_name = 'Pizza'
        self.price = 15

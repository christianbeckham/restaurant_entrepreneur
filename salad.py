from order import Order


class Salad(Order):
    def __init__(self):
        super().__init__()
        self.dish_name = 'Salad'
        self.price = 5

from pizza import Pizza
from pasta import Pasta
from salad import Salad


class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(order_type):
        if order_type == 'Pizza':
            return Pizza()
        elif order_type == 'Pasta':
            return Pasta()
        elif order_type == 'Salad':
            return Salad()
        else:
            print('Invalid order.')

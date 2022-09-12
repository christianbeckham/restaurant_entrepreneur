from pizza import Pizza
from pasta import Pasta
from salad import Salad


class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(order_type):
        order_type_lowercase = order_type.lower()

        if order_type_lowercase == 'pizza':
            return Pizza()
        elif order_type_lowercase == 'pasta':
            return Pasta()
        elif order_type_lowercase == 'salad':
            return Salad()
        else:
            print('Invalid order.')

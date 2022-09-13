from pizza import Pizza
from pasta import Pasta
from salad import Salad


class OrderFactory:
    '''A class to represent an Order Factory.

    This class implements the Factory Design Pattern.

    Attributes:
        None
    '''

    def __init__(self):
        pass

    @staticmethod
    def create_order(order_type):
        '''Create and return a class intance defined by an order type.

        *This is a static method.

        Args:
            order_type: A string representing the type of class to instantiate.

        Return:
            ChildClass(Order)
        '''
        order_type_lowercase = order_type.lower()

        if order_type_lowercase == 'pizza':
            return Pizza()
        elif order_type_lowercase == 'pasta':
            return Pasta()
        elif order_type_lowercase == 'salad':
            return Salad()
        else:
            print('Invalid order type.')

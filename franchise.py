from logger import logger
from order_factory import OrderFactory


class Franchise:
    '''A class to represent a franchise.

    Attributes:
        location_number: An integer indicating the franchise location number.
    '''

    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        '''Places an order from a franchise.

        Prompts a user for an order, dispatches the order to the OrderFactory class, and logs the transaction.

        Args:
            None

        Return:
            None
        '''
        print(f'\nWelcome to Franchise #{self.location_number}!')
        print('What would you like to order?')
        print(f'\t1 - Pizza\n\t2 - Pasta\n\t3 - Salad')
        user_order = (False, None)

        while user_order[0] is False:
            prompt_input_number = int(input('Enter order number: '))
            user_order = self.validate_order_input_number(
                prompt_input_number)

        new_order = OrderFactory.create_order(user_order[1])
        logger.log_transaction(new_order, self.location_number)

    def validate_order_input_number(self, input_number):
        '''Validates the user order number entered from the input prompt.

        Args:
            input_number: An integer representing the input number to validate.

        Return:
            Returns a tuple.
        '''
        options = {
            1: (True, 'Pizza'),
            2: (True, 'Pasta'),
            3: (True, 'Salad'),
        }
        return options.get(input_number, (False, None))

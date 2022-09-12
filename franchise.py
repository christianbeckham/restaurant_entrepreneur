from logger import logger
from order_factory import OrderFactory


class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        print(
            f'What would you like to order from store #{self.location_number}?')
        print(f'\t1 - Pizza\n\t2 - Pasta\n\t3 - Salad')
        user_order = (False, None)

        while user_order[0] is False:
            prompt_input_number = int(input('\nEnter order number: '))
            user_order = self.__validate_order_input_number(
                prompt_input_number)

        new_order = OrderFactory.create_order(user_order[1])
        logger.log_transaction(new_order, self.location_number)

    def __validate_order_input_number(self, input_number):
        options = {
            1: (True, 'Pizza'),
            2: (True, 'Pasta'),
            3: (True, 'Salad'),
        }

        return options.get(input_number, (False, None))

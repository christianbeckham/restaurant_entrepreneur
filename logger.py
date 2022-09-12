class Logger:
    '''Provide functionality to log transactions.

    This class is instantiated in this file and implemented using the Singleton design pattern.

    Attributes:
        transaction_count: An integer to keep track of the total number of transactions.
        daily_sales: An integer to keep track of the total amount of daily sales.
    '''

    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, store_number):
        '''Logs a transaction to a file.

        Enters a new transaction as a row in the log.txt file. The 'total_number_of_lines_in_a_file' is a helper method used to sequentially continue the transaction count.

        Args:
            order: An Order instance.
            store_number: An integer.

        Returns:
            None
        '''
        self.transaction_count = self.total_number_of_lines_in_a_file() + 1
        self.daily_sales += order.price

        with open('log.txt', 'a') as log_file:
            log_file.write(
                f'ORDER#{self.transaction_count},{order.dish_name},STORE#{store_number},ITEM${order.price},TOTAL${self.daily_sales}\n')

    def total_number_of_lines_in_a_file(self):
        '''Retrieve the total number of lines in a file.

        Reads all of the lines in a file and returns the total count.

        Args:
            None
        Return:
            Integer representing the total number of rows in the file.
        '''
        with open('log.txt', 'r') as file:
            file_lines = file.readlines()
            return len(file_lines)


logger = Logger()

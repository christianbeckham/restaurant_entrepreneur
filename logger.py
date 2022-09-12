class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_sales += order.price

        with open('log.txt', 'a') as log_file:
            log_file.write(
                f'ORDER#{self.transaction_count},{order.dish_name},STORE#{store_number},ITEM${order.price},TOTAL${self.daily_sales}\n')
            log_file.close()


logger = Logger()

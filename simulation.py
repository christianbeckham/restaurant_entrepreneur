from franchise import Franchise


class Simulation:
    '''A class to start the simulation process of the application.

    This class implements the Facade Design Pattern.

    Attributes:
        None
    '''

    def __init__(self):
        pass

    def run_simulation(self):
        '''Starts running the simulation.

        Args:
            None

        Return:
            None
        '''
        franchise_one = Franchise(1)
        franchise_two = Franchise(2)
        franchise_three = Franchise(3)

        franchise_one.place_order()
        franchise_two.place_order()
        franchise_three.place_order()

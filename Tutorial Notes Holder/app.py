class PizzaUndeliveredError(Exception):
    def __init__(self, message):
        self.message = message
# raising the error:
raise PizzaUndeliveredError('The pizza has still not been delivered.')
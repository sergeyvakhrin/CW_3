class Operation:

    def __init__(self, date: str, amount: str, currency_name: str, description: str, from_: str, to: str):
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to

    def __srt__(self):
        pass

    def __pepr__(self):
        pass

    def sorted_instances(self):
        """

        """
        pass

    def get_quantity_operation(self, quantity):
        """
        Получение определенного размера списка экземпляров класса
        """
        self.quantity = quantity

        return
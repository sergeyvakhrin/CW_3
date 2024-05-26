from datetime import datetime


class Operation:

    def __init__(self, date: str, amount: str, currency_name: str, description: str, from_: str, to: str):
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to

    def __str__(self):
        return (f'{self.change_date_format()} {self.description}\n'
                f'{self.hide_number_from()}{self.hide_number_to()}\n'
                f'{self.amount} {self.currency_name}')

    # def __repr__(self):
    #     pass

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def change_date_format(self):
        """
        приобразовнаие даты в формат по заданию 14.10.2018
        """
        the_date = datetime.fromisoformat(self.date)
        return the_date.strftime("%d.%m.%Y")

    def hide_number_from(self):
        """
        скрытие номера счета списания
        """
        if self.from_ != "":
            hide_from = self.from_.split(" ")
            hide_from[-1] = f'{hide_from[-1][:4]} {hide_from[-1][5:7]}** **** {hide_from[-1][-4:]} -> '
            return " ".join(hide_from)
        else:
            return ""

    def hide_number_to(self):
        """
        скрытие номера счета зачисления
        """
        hide_to = self.to.split(" ")
        hide_to[-1] = f'**{hide_to[-1][-4:]}'
        return " ".join(hide_to)

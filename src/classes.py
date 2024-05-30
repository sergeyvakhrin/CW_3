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
                f'{self.hide_number(self.from_)}{self.deliter()}{self.hide_number(self.to)}\n'
                f'{self.amount} {self.currency_name}')

    def __repr__(self):
        return (f'{self.change_date_format()} {self.description}\n'
                f'{self.hide_number(self.from_)}{self.deliter()}{self.hide_number(self.to)}\n'
                f'{self.amount} {self.currency_name}')

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

    def hide_number(self, account_number: str) -> str:
        """
        скрытие номера счета
        """
        if account_number != "":
            account_type: list[str] = account_number.split(" ")
            number: str = account_type[-1]

            if account_type[0] == "Счет":
                hide_number: str = f'**{number[-4:]}'
            if account_type[0] != "Счет":
                hide_number: str = f'{number[:4]} {number[4:6]}** **** {number[-4:]}'

            account_type[-1] = hide_number
            return " ".join(account_type)
        else:
            return ""

    def deliter(self):
        if self.from_:
            return f' -> '
        else:
            return f''

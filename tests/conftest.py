import pytest

from src.classes import Operation


@pytest.fixture
def operation():
    return Operation(
            date="2019-08-26T10:50:58.294041",
            amount="31957.58",
            currency_name="руб.",
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589"
    )


@pytest.fixture
def operations():
    return [Operation(
            date="2019-07-03T18:35:29.512364",
            amount="31957.58",
            currency_name="руб.",
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589"
            ),
            Operation(
            date="2018-06-30T02:08:58.425572",
            amount="31957.58",
            currency_name="руб.",
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589"
            ),
            Operation(
            date="2020-03-23T10:45:06.972075",
            amount="31957.58",
            currency_name="руб.",
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589"
            )
    ]

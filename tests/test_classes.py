def test_operation_init(operation):
    assert operation.from_ == "Maestro 1596837868705199"
    assert operation.date == "2019-08-26T10:50:58.294041"
    assert operation.amount == "31957.58"
    assert operation.currency_name == "руб."
    assert operation.description == "Перевод организации"
    assert operation.to == "Счет 64686473678894779589"


def test_change_date_format(operation):
    assert isinstance(operation.change_date_format(), str)
    assert operation.change_date_format() == "26.08.2019"


def test_hide_number(operation):
    assert operation.hide_number(operation.from_) == "Maestro 1596 83** **** 5199"
    assert operation.hide_number(operation.to) == "Счет **9589"


def test_str(operation):
    assert str(operation) == (f"26.08.2019 Перевод организации\n"
                              f"Maestro 1596 83** **** 5199 -> Счет **9589\n"
                              f"31957.58 руб.")


def test_repr(operation):
    assert repr(operation) == (f"26.08.2019 Перевод организации\n"
                              f"Maestro 1596 83** **** 5199 -> Счет **9589\n"
                              f"31957.58 руб.")


def test_deliter(operation):
    assert operation.deliter() == " -> "
import json
import os.path
from pathlib import Path

from config import RESULT_OPERATOINS
from src.classes import Operation


def load_data(path: Path):
    """
    загрузка данных из файла
    """
    if os.path.exists(path):
        with open(path, "rt", encoding="UTF-8") as file:
            return json.load(file)
    else:
        print("Отсутствуют данные")
        return {}


def get_instances_executed(operations_list) -> list:
    """
    получаем список экземпляров классов успешных операций
    """
    instances_list: list = []
    for operation in operations_list:
        if operation.get("state") == RESULT_OPERATOINS:
            # инициализируем экземпляр класса
            operation = Operation(
                date=operation["date"],
                amount=operation["operationAmount"]["amount"],
                currency_name=operation["operationAmount"]["currency"]["name"],
                description=operation["description"],
                from_=operation.get("from") if operation.get("from") is not None else "",
                to=operation["to"]
            )
        else:
            continue
        # добавляем экземпляр класса в список
        instances_list.append(operation)
    return instances_list


def sorted_instances(instances_list_to_sort):
    """
    сортировка списка классов по дате
    """
    return sorted(instances_list_to_sort, reverse=True)


from config import DATA_PATH, QUANTITY_OPERATIONS
from src.utils import load_data, get_instances_executed, sorted_instances


def main():
    # загружаем данный из файла
    operations_list: list[dict] = load_data(DATA_PATH)

    # получаем список экземпляров классов успешных операций
    executed_operations: list = get_instances_executed(operations_list)

    # сортируем список экземпляров классов по дате
    sorted_operations = sorted_instances(executed_operations)

    # получение списка последних успешных операций
    quantity_operations = sorted_operations[:QUANTITY_OPERATIONS]

    # вывод последних успешных операций
    for quantity_operation in quantity_operations:
        print(f'{quantity_operation}\n')


if __name__ == '__main__':
    main()

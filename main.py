from config import DATA_PATH
from src.utils import load_data, instances_executed


# загружаем данный из файла
operations_list: list[dict] = load_data(DATA_PATH)

# получаем список экземпляров классов успешных операций
executed_operations: list = instances_executed(operations_list)


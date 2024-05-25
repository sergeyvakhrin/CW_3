import json
from pathlib import Path


def load_data(path: Path):
    """
    загрузка данных из файла
    """

    with open(path, "rt", encoding="UTF-8") as file:
        return json.load(file)




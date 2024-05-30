from src.utils import get_instances_executed, sorted_instances
from tests.test_data import test_list_dict1, test_list_dict2


def test_load_data():
    # проверить, что приходит json
    pass


def test_get_instances_executed(operations):
    assert get_instances_executed(test_list_dict1) == []
    assert get_instances_executed(test_list_dict2) == []


def test_sorted_instances(operations):
    assert sorted_instances([4, 3, 7, 6]) == [7, 6, 4, 3]
    assert sorted_instances(["a", "z", "b", "y"]) == ["z", "y", "b", "a"]
    assert isinstance(sorted_instances(operations), list)
    assert len(sorted_instances(operations)) == 3
    assert sorted_instances(operations)[0].date == "2020-03-23T10:45:06.972075"

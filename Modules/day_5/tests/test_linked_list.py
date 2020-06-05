import pytest
from Modules.day_5.day_5.linked_list.linked_list import LinkedList
from Modules.day_5.day_5.linked_list.node import Node


@pytest.fixture
def sample_linked_list():
    ll = LinkedList()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("orange")
    return ll


def test_linked_list_str(sample_linked_list):
    assert str(sample_linked_list) == "\"{ orange } -> { banana } -> { apple } -> NULL\""


def test_linked_list_insert(sample_linked_list):
    sample_linked_list.insert("kiwi")
    assert sample_linked_list.includes("kiwi")

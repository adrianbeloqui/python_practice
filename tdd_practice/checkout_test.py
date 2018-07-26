import pytest

from tdd_practice.checkout import Checkout


@pytest.fixture()
def checkout():
    co = Checkout()
    co.add_item_price("a", 1)
    co.add_item_price("b", 2)
    return co


def test_can_calculate_current_total(checkout):
    checkout.add_item("a")
    assert checkout.calculate_current_total() == 1


def test_get_correct_total_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_current_total() == 3


def test_can_add_discout(checkout):
    checkout.add_discount("a", 3, 2)

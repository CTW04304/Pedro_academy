import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import get_highest_number


def test_find_highest_number():
    list_1 = [1, 2, 3, 4, 5]
    highest_1 = get_highest_number(list_1)

    assert highest_1 == 5

    list_2 = [50, 100, 949, 345, 745]
    highest_2 = get_highest_number(list_2)

    assert highest_2 == 949


@pytest.mark.parametrize(
    "list_numbers, highest_value",
    [
        ([1, 2, 3, 4, 5], 5),
        ([50, 100, 949, 345, 745], 949)
    ],
    ids=["highest_1", "highest_2"]
)
def test_find_highest_number_2(list_numbers, highest_value):
    assert get_highest_number(list_numbers) == highest_value
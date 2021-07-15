import pytest
from item import ItemBase


class TestItem:

    @pytest.mark.parametrize("args, results", [
        pytest.param(
            (4.7, 1), ValueError, id='count is float'
        ),
        pytest.param(
            (-5, 1), ValueError, id='count is negative'
        ),
        pytest.param(
            (5, -1), ValueError, id='weight is negative'
        )
    ])
    def test_values(self, args, results):
        with pytest.raises(results):
            ItemBase(
                name="book",
                country_of_origin="RU",
                count=args[0],
                weight=args[1]
            )

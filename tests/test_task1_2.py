import pytest
from src.task1_2 import get_cost


@pytest.mark.parametrize('weight, expected',
                        ((10, 'Стоимость доставки: 200 руб.'),
                        (20, 'Стоимость доставки: 500 руб.'))
)

def test_get_cost(weight, expected):
    assert get_cost(weight) == expected, 'Ошибка'

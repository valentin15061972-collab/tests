import pytest
from src.task1_1 import check_age


@pytest.mark.parametrize('age, expected',
                        ((15, 'Доступ запрещён'),
                        (25, 'Доступ разрешён'))
)


def test_check_age(age, expected):
    assert check_age(age) == expected, 'Ошибка'

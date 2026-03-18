import pytest
from src.task1_3 import check_auth


@pytest.mark.parametrize('login, password, expected', (
    ('admin', 'password', 'Добро пожаловать'),
    ('Admin', 'password', 'Доступ ограничен')
))

def test_check_auth(login, password, expected):
    assert check_auth(login, password) == expected, 'Ошибка'

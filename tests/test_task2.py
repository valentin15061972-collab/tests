import pytest
from src.task2 import create_folder_yd


@pytest.fixture
def env_var(monkeypatch):
    monkeypatch.setenv('YD_TOKEN', "test_oauth_token")


def test_create_folder_yd_success(env_var, requests_mock):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    requests_mock.put(url, status_code=201)

    result = create_folder_yd("test_folder_name")

    assert result == 201



def test_create_folder_yd_failure(env_var, requests_mock):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    requests_mock.put(url,  status_code=400)

    result = create_folder_yd("invalid_folder_name")

    assert result == 400

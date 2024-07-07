import pytest


@pytest.fixture
def setup():
    print("Начало теста")
    yield
    print("Конец теста")

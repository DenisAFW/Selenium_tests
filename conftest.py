# Задание 1. Оптимизация примера из лекции
# Доработать пример из лекции следующим образом:
# вынести все локаторы элементов в фикстуры в conftest.py
# вынести ожидаемый результат в фикстуру в conftest.py
# добавить завершение работы Selenium после теста
# вынести время ожидания в конфигурационный файл testdata.yaml


import yaml
from module import Site
import pytest

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def x_selector1():
    return data["input_login"]


@pytest.fixture()
def x_selector2():
    return data["input_passwd"]


@pytest.fixture()
def x_selector3():
    return data["correct_input"]


@pytest.fixture()
def btn_selector():
    return data["css_btn"]


@pytest.fixture()
def err_selector():
    return data["error"]


@pytest.fixture()
def correct_res():
    return "401"


@pytest.fixture()
def result():
    return f"Hello, {data['user']}"


@pytest.fixture()
def create_post():
    return data["plus"]


@pytest.fixture()
def title():
    return data["title"]


@pytest.fixture()
def description():
    return data["description"]


@pytest.fixture()
def content():
    return data["content"]


@pytest.fixture()
def save_button():
    return data["save"]


@pytest.fixture()
def title_post():
    return data["title_post"]


@pytest.fixture()
def check_2():
    return "For Emperor!"


@pytest.fixture()
def del_post():
    return data["delete_btn"]


@pytest.fixture()
def check_posts():
    return data["posts"]

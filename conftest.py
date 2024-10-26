import time
import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from framework.wait_page import Wait
from framework.page_fixture import PageFixture
from test_data.test_data import DataGenerator
from framework.api_page.petstore_user_method import PetStoreUser
from framework.api_page.petstore_pet_method import PetStorePet
from framework.api_page.petstore_order_method import PetStoreOrder
import psycopg2
from settings import database_config


@pytest.fixture
def driver():
    """
        Фикстура для создания веб-драйвера Chrome с опцией headless.

        Фикстура создает экземпляр веб-драйвера Chrome с опцией headless, что означает,
        что браузер будет работать в фоновом режиме без графического интерфейса.
        Устанавливается неявное ожидание в 5 секунд для ожидания элементов на странице.
        После выполнения тестов веб-драйвер закрывается.
    """

    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def pytest_runtest_teardown(item, nextitem):
    """
        Хук pytest, который выполняется после завершения каждого теста.
        Если в тесте использовался WebDriver, захватывает скриншот экрана и сохраняет его в директорию
        'results/screenshots' и прикрепляет его к отчету Allure.

        Параметры:
        - item: объект теста, содержащий информацию о только что выполненном тесте.
        - nextitem: объект следующего теста (не используется в этой функции).

        Логика работы:
        1. Извлечение объекта WebDriver из аргументов текущей тестовой функции.
        2. Проверка, был ли WebDriver использован в тесте.
        3. Создание директории для скриншотов, если она не существует.
        4. Формирование имени файла для скриншота на основе имени теста.
        5. Захват и сохранение скриншота.
        6. Прикрепление скриншота к отчету Allure.
    """

    driver = item.funcargs.get('driver')
    if driver:
        # Создаем директорию для сохранения скриншотов, если она не существует
        screenshots_dir = os.path.join('results')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Создаем имя файла для скриншота
        test_name = item.name
        screenshot_file = os.path.join(screenshots_dir, f"{test_name}.png")

        # Захватываем и сохраняем скриншот
        driver.save_screenshot(screenshot_file)

        # Прикрепляем скриншот к отчету Allure
        with open(screenshot_file, 'rb') as image_file:
            allure.attach(image_file.read(), name=test_name, attachment_type=allure.attachment_type.PNG)


@pytest.fixture
def slow_scroll():
    """
        Фикстура slow_scroll предназначена для медленной прокрутки страницы вниз.
        Эта фикстура создает функцию scroll, которая прокручивает страницу вниз с заданным шагом и паузой
        между прокрутками.
    """

    def scroll(driver, scroll_step=150, pause_duration=0.3):
        """
            Функция scroll прокручивает страницу вниз.

            :param driver: Драйвер браузера Selenium.
            :param scroll_step: Величина прокрутки страницы вниз на каждом шаге (по умолчанию 150 пикселей).
            :param pause_duration: Длительность паузы между прокрутками (по умолчанию 0.3 секунды).
        """
        current_position = driver.execute_script('return window.pageYOffset')
        page_height = driver.execute_script('return document.body.scrollHeight')

        while current_position < page_height:
            current_position += scroll_step
            driver.execute_script(f'window.scrollTo(0, {current_position})')
            time.sleep(pause_duration)

    return scroll


@pytest.fixture
def scroll_down(driver):
    """ Фикстура для прокрутки страницы вниз на заданное количество пикселей. """

    def _scroll(pixels):
        """
            Функция _scroll: которая прокручивает страницу на указанное количество пикселей.

            :param pixels: Количество пикселей, на которое следует прокрутить страницу.
            :return: Функция _scroll, которая прокручивает страницу на указанное количество пикселей.
        """
        driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(1.5)

    return _scroll


@pytest.fixture
def wait(driver):
    """
        Фикстура wait создает объект ожидания (WebDriverWait) для ожидания определенного условия веб-элемента.

        :param driver: Драйвер браузера Selenium.
        :return: Объект ожидания (WebDriverWait).
    """
    return Wait(driver)


@pytest.fixture
def page_fixture(driver):
    """
        Фикстура page_fixture создает экземпляр объекта PageFixture, который представляет страницу веб-приложения.

        :param driver: Драйвер браузера Selenium.
        :return: Экземпляр объекта PageFixture.
    """
    return PageFixture(driver)


@pytest.fixture
def text_box_form_data(driver):
    """
        :param Фикстура для получения тестовых данных для формы с данными.
        :returns: TestData: Экземпляр класса TestData с тестовыми данными.
    """
    return DataGenerator()


@pytest.fixture
def registration_form_data(driver):
    """
        :param Фикстура для получения тестовых данных для формы с данными.
        :returns: TestData: Экземпляр класса TestData с тестовыми данными.
    """
    return DataGenerator()


@pytest.fixture
def user_test_data():
    """ Фикстура для предоставления тестовых данных. """
    return DataGenerator()


@pytest.fixture
def test_data():
    return DataGenerator()


@pytest.fixture
def pet_store_user_fixture():
    """ Фикстура для предоставления методов для взаимодействия с API магазина домашних животных. """
    return PetStoreUser()


@pytest.fixture
def pet_store_pet_fixture():
    """ Фикстура для предоставления методов для взаимодействия с API магазина домашних животных. """
    return PetStorePet()


@pytest.fixture
def order_store_pet_fixture():
    """ Фикстура для создания экземпляра класса PetStoreOrder для тестирования операций заказа. """

    return PetStoreOrder()


@pytest.fixture
def db_connection():
    """
        Фикстура для создания подключения к базе данных PostgreSQL.

        Returns:
            psycopg2.extensions.connection: Объект подключения к базе данных PostgreSQL.
    """
    connection = None
    try:
        db_config = {
            "dbname": database_config.dbname,
            "user": database_config.user,
            "password": database_config.password,
            "host": database_config.host,
            "port": database_config.port
        }
        connection = psycopg2.connect(**db_config)
        yield connection
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


@pytest.fixture
def db_connection_db_postgres():
    """
        Фикстура для создания подключения к другой базе данных PostgreSQL.

        Returns:
            psycopg2.extensions.connection: Объект подключения к другой базе данных PostgreSQL.
    """
    connection = None
    try:
        db_config = {
            "dbname": database_config.other_dbname,
            "user": database_config.user,
            "password": database_config.password,
            "host": database_config.host,
            "port": database_config.port
        }
        connection = psycopg2.connect(**db_config)
        yield connection
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


@pytest.fixture
def db_test_data():
    """ Фикстура для создания тестовых данных. """
    return DataGenerator()


@pytest.fixture
def student_registration_form():
    """ Фикстура для создания тестовых данных. """
    return DataGenerator()

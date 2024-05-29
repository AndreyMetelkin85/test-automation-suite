import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from framework.wait_page import Wait
from framework.page_fixture import PageFixture
from test_data.test_data import DataGenerator
from framework.api_page.petstore_user_method import PetStoreUser
from framework.api_page.petstore_pet_method import PetStorePet
from framework.api_page.petstore_order_method import PetStoreOrder
import psycopg2
from dotenv import load_dotenv


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


# Хук для захвата скриншота после каждого теста
def pytest_runtest_teardown(item, nextitem):
    """
        Хук pytest, который выполняется после завершения каждого теста.
        Если в тесте использовался WebDriver, захватывает скриншот экрана и сохраняет его в директорию 'screenshots'.

        Параметры:
        - item: объект теста, содержащий информацию о только что выполненном тесте.
        - nextitem: объект следующего теста (не используется в этой функции).

        Логика работы:
        1. Извлечение объекта WebDriver из аргументов текущей тестовой функции.
        2. Проверка, был ли WebDriver использован в тесте.
        3. Создание директории для скриншотов, если она не существует.
        4. Формирование имени файла для скриншота на основе имени теста.
        5. Захват и сохранение скриншота.
    """

    driver = item.funcargs.get('driver')
    if driver:
        # Создаем директорию для сохранения скриншотов, если она не существует
        screenshots_dir = 'screenshots'
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Создаем имя файла для скриншота
        test_name = item.name
        screenshot_file = os.path.join(screenshots_dir, f"{test_name}.png")

        # Захватываем и сохраняем скриншот
        driver.save_screenshot(screenshot_file)


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
    """
       Фикстура для прокрутки страницы вниз на заданное количество пикселей.
    """

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
def perform_double_click(driver):
    """
        Фикстура perform_double_click предназначена для выполнения двойного клика на элементе веб-страницы.

        Данная фикстура создает функцию double_click, которая выполняет двойной клик на указанном элементе.
        Для этого используется объект ActionChains, который инициализируется с переданным драйвером.

        :param driver: Драйвер браузера Selenium.
    """

    def double_click(element):
        """
                Функция double_click выполняет двойной клик на элементе веб-страницы.

                :param element: Элемент веб-страницы, на который нужно выполнить двойной клик.
        """
        action_chains = ActionChains(driver)
        action_chains.double_click(element).perform()

    return double_click


@pytest.fixture
def perform_right_click(driver):
    """
        Фикстура perform_right_click предназначена для выполнения правого клика на элементе веб-страницы.

        Данная фикстура создает функцию right_click, которая выполняет правый клик на указанном элементе.
        Для этого используется объект ActionChains, который инициализируется с переданным драйвером.

        :param driver: Драйвер браузера Selenium.
    """

    def right_click(element):
        """
            Функция right_click выполняет правый клик на элементе веб-страницы.

            :param element: Элемент веб-страницы, на который нужно выполнить правый клик.
        """
        action_chains = ActionChains(driver)
        action_chains.context_click(element).perform()

    return right_click


@pytest.fixture
def perform_normal_click(driver):
    """
        Фикстура perform_normal_click предназначена для выполнения обычного (левого) клика на элементе веб-страницы.

        Данная фикстура создает функцию normal_click_action, которая выполняет обычный (левый) клик на указанном элементе.
        Для этого используется объект ActionChains, который инициализируется с переданным драйвером.

        :param driver: Драйвер браузера Selenium.

    """

    def normal_click_action(element):
        """
            Функция normal_click_action выполняет обычный (левый) клик на элементе веб-страницы.

            :param element: Элемент веб-страницы, на который нужно выполнить обычный (левый) клик.
        """
        action_chains = ActionChains(driver)
        action_chains.click(element).perform()

    return normal_click_action


@pytest.fixture
def user_test_data():
    """
        Фикстура для предоставления тестовых данных.
    """
    return DataGenerator()


@pytest.fixture
def pet_test_data():
    """
        Фикстура для предоставления тестовых данных.
    """
    return DataGenerator()


@pytest.fixture
def order_test_data():
    """
        Фикстура для предоставления тестовых данных для заказа.
    """
    return DataGenerator()


@pytest.fixture
def pet_store_user_fixture():
    """
         Фикстура для предоставления методов для взаимодействия с API магазина домашних животных.
    """
    return PetStoreUser()


@pytest.fixture
def pet_store_pet_fixture():
    """
        Фикстура для предоставления методов для взаимодействия с API магазина домашних животных.
    """
    return PetStorePet()


@pytest.fixture
def order_store_pet_fixture():
    """
        Фикстура для создания экземпляра класса PetStoreOrder для тестирования операций заказа.
    """

    return PetStoreOrder()


@pytest.fixture
def db_connection():
    """
        Фикстура для создания подключения к базе данных PostgreSQL.

        Returns:
            psycopg2.extensions.connection: Объект подключения к базе данных PostgreSQL.
    """
    connection = None
    load_dotenv()
    try:
        db_config = {
            "dbname": os.environ["DBNAME"],
            "user": os.environ["USER"],
            "password": os.environ["PASSWORD"],
            "host": os.environ["HOST"],
            "port": os.environ["PORT"]
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
    load_dotenv()
    try:
        db_config = {
            "dbname": os.environ["OTHER_DBNAME"],
            "user": os.environ["USER"],
            "password": os.environ["PASSWORD"],
            "host": os.environ["HOST"],
            "port": os.environ["PORT"]
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
    """
        Фикстура для создания тестовых данных.
    """
    return DataGenerator()


@pytest.fixture
def student_registration_form():
    return DataGenerator()

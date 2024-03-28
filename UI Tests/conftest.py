import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from framework.pages.website_stenn.main_page import MainPage
from framework.wait_page import Wait
from framework.page_fixture import PageFixture


@pytest.fixture
def driver():
    # Создание экземпляра объекта Options для управления параметрами запуска браузера
    options = Options()
    options.add_argument("--start-maximized")

    # Инициализация веб-драйвера Chrome с переданными опциями
    driver = webdriver.Chrome(options=options)

    # Установка неявного ожидания в 5 секунд
    driver.implicitly_wait(5)

    # Создание экземпляра главной страницы, передавая веб-драйвер
    base_page = MainPage(driver)
    base_page.go_to_site()  # Переход на сайт

    # Возвращение драйвера для использования в тестах
    yield driver

    # Закрытие веб-драйвера после завершения теста
    driver.quit()


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

            :param driver - Драйвер браузера Selenium.
            :param scroll_step - Величина прокрутки страницы вниз на каждом шаге (по умолчанию 150 пикселей).
            :param pause_duration - Длительность паузы между прокрутками (по умолчанию 0.3 секунды).
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
            Функция _scroll - которая прокручивает страницу на указанное количество пикселей.

            :param pixels: Количество пикселей, на которое следует прокрутить страницу.
        """
        driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(1.5)

    return _scroll


@pytest.fixture
def wait(driver):
    """
        Фикстура wait создает объект ожидания (WebDriverWait) для ожидания определенного условия веб-элемента.

        :param driver: Драйвер браузера Selenium.
    """
    return Wait(driver)


@pytest.fixture
def page_fixture(driver):
    """
        Фикстура page_fixture создает экземпляр объекта PageFixture, который представляет страницу веб-приложения.

        :param driver: Драйвер браузера Selenium.
    """
    return PageFixture(driver)

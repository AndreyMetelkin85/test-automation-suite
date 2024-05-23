from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC
import logging
from utils import highlight, highlights


class BasePage(ABC):
    """
        Базовый класс для страниц веб-сайта.

        Атрибуты:
            driver: Экземпляр веб-драйвера для управления браузером.
            stenn_url (str): URL-адрес сайта Stenn.
            demo_qa_url (str): URL-адрес сайта DemoQA.
    """

    def __init__(self, driver):
        self.driver = driver
        self.stenn_url = "https://stenn.com/"
        self.demo_qa_url = 'https://demoqa.com/'
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(console_handler)

    @highlight
    def find_element(self, locator, time=10):
        """
            Метод для поиска одного элемента на странице.

            :param locator: Локатор элемента.
            :param time: Время ожидания (по умолчанию 10 секунд).
        """
        self.logger.info(f"Поиск элемента с локатором: {locator}, время ожидания: {time} секунд")
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Не удалось найти элемент с локатором {locator}")
            self.logger.info(f"Элемент найден: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элемента с локатором {locator}: {e}")
            raise

    @highlights
    def find_elements(self, locator, time=10):
        """
            Метод для поиска всех элементов на странице.

            :param locator: Локатор элементов.
            :param time: Время ожидания (по умолчанию 10 секунд).
        """
        self.logger.info(f"Поиск всех элементов с локатором: {locator}, время ожидания: {time} секунд")
        try:
            elements = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Не удалось найти элементы с локатором {locator}"
            )
            self.logger.info(f"Элементы найдены: {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элементов с локатором {locator}: {e}")
            raise

    def go_to_element(self, element):
        """
            Прокручивает страницу к указанному элементу.
            :param element: Элемент, к которому нужно прокрутить страницу.
        """
        self.logger.debug(f"Прокрутка страницы к элементу: {element}")
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.debug(f"Прокрутка к элементу выполнена успешно: {element}")
        except Exception as e:
            self.logger.error(f"Ошибка при прокрутке к элементу: {e}")
            raise

    def go_to_web_site_stenn(self):
        """
            Метод для перехода на главную страницу сайта "https://stenn.com/".
        """
        self.logger.debug(f"Переход на сайт: {self.stenn_url}")
        try:
            self.driver.get(self.stenn_url)
            self.logger.debug(f"Успешный переход на сайт: {self.stenn_url}")
        except Exception as e:
            self.logger.error(f"Ошибка при переходе на сайт {self.stenn_url}: {e}")
            raise

    def go_to_web_site_demo_qa(self):
        """
            Метод для перехода на главную страницу сайта 'https://demoqa.com/'.
        """
        self.logger.debug(f"Переход на сайт: {self.demo_qa_url}")
        try:
            self.driver.get(self.demo_qa_url)
            self.logger.debug(f"Успешный переход на сайт: {self.demo_qa_url}")
        except Exception as e:
            self.logger.error(f"Ошибка при переходе на сайт {self.demo_qa_url}: {e}")
            raise

    def get_heading_label(self):
        """
            Абстрактный метод для получения заголовка страницы.
        """
        self.logger.debug("Вызов абстрактного метода get_heading_label")
        pass

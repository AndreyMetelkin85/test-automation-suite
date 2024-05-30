import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC
from framework.logger_config import setup_logger
from framework.selenium_utils.elements import BaseElement


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
        self.logger = setup_logger(self.__class__.__name__)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(console_handler)

    def find_element(self, locator, time=10):
        """
              Поиск элемента с указанным локатором.

              Метод выполняет поиск элемента на странице с использованием заданного локатора и времени ожидания.
              Если элемент найден, возвращается объект BaseElement. В случае ошибки при поиске,
              исключение будет логироваться
              и поднято для обработки в вызывающем коде.

              Параметры:
              - locator: tuple, локатор искомого элемента (например, (By.ID, 'element_id')).
              - time: int, время ожидания элемента в секундах (по умолчанию 10 секунд).

              Возвращает:
              - BaseElement: объект найденного элемента.

              Логирование:
              - Информация об успешном поиске элемента.
              - Ошибка, если элемент не найден.

              Исключения:
              - Raise Exception: если элемент не найден в течение заданного времени.
        """
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
            self.logger.info(f"Элемент найден: {locator}")
            return BaseElement(element, locator)
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элемента с локатором {locator}: {e}")
            raise

    def find_elements(self, locator, time=10):
        """
             Поиск всех элементов с указанным локатором.

             Метод выполняет поиск всех элементов на странице с использованием заданного локатора и времени ожидания.
             Если элементы найдены, возвращается список объектов BaseElement. В случае ошибки при поиске,
             исключение будет логироваться и поднято для обработки в вызывающем коде.

             Параметры:
             - locator: tuple, локатор искомых элементов (например, (By.CLASS_NAME, 'element_class')).
             - time: int, время ожидания элементов в секундах (по умолчанию 10 секунд).

             Возвращает:
             - list[BaseElement]: Список объектов найденных элементов.

             Логирование:
             - Информация об успешном поиске элементов.
             - Ошибка, если элементы не найдены.

             Исключения:
             - Raise Exception: если элементы не найдены в течение заданного времени.
        """
        try:
            elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
            self.logger.info(f"Элементы найдены: {locator}")
            return [BaseElement(element, locator) for element in elements]
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элементов с локатором {locator}: {e}")
            raise

    def go_to_element(self, element):
        """
            Прокручивает страницу к указанному элементу.
            :param element: Элемент, к которому нужно прокрутить страницу.
        """
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

import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger_config import setup_logger
from framework.selenium_utils.elements import BaseElement
from settings import base_config


class BasePage:
    """
           Базовый класс для страниц веб-сайта.

           Атрибуты:
               driver: Экземпляр веб-драйвера для управления браузером.
               stenn_url (str): URL-адрес сайта Stenn.
               demo_qa_url (str): URL-адрес сайта DemoQA.
               logger: Экземпляр логгера для ведения логов.

           Методы:
           __init__(driver): Инициализирует базовую страницу с заданным веб-драйвером.
    """

    def __init__(self, driver):
        """
              Инициализирует базовую страницу с заданным веб-драйвером.

              Параметры:
              - driver: Экземпляр веб-драйвера для управления браузером.

              Логика:
              1. Инициализирует веб-драйвер.
              2. Устанавливает URL-адреса сайтов Stenn и DemoQA.
              3. Настраивает логгер для класса.
              4. Добавляет обработчик логов для вывода в консоль, если он еще не добавлен.
        """
        self.driver = driver
        self.demo_qa_url = base_config.base_url_demoqa

        # Создает и настраивает логгер для текущего класса, используя имя класса в качестве имени логгера.
        self.logger = setup_logger(self.__class__.__name__)

        # # Создает обработчик логирования, который выводит логи в стандартный поток (обычно консоль).
        # console_handler = logging.StreamHandler()
        #
        # # Устанавливает уровень логирования для консольного обработчика на DEBUG, что означает,
        # # что все сообщения уровня DEBUG и выше будут выводиться в консоль.
        # console_handler.setLevel(logging.DEBUG)
        #
        # # Создает объект форматирования логов, который определяет формат сообщений логов.
        # # В данном случае формат включает время записи лог-сообщения, имя логгера, уровень логирования и само сообщение.
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #
        # # Применяет созданный форматтер к консольному обработчику.
        # console_handler.setFormatter(formatter)
        #
        # # Проверяет, есть ли уже обработчики, присоединенные к логгеру.
        # # Если обработчиков нет, добавляет созданный консольный обработчик к логгеру.
        # # Это предотвращает добавление нескольких одинаковых обработчиков, если инициализация логгера
        # # происходит несколько раз.
        # if not self.logger.handlers:
        #     self.logger.addHandler(console_handler)

    def find_element(self, locator, time=10):
        """
              Поиск элемента с указанным локатором.

              Метод выполняет поиск элемента на странице с использованием заданного локатора и времени ожидания.
              Если элемент найден, возвращается объект BaseElement. В случае ошибки при поиске,
              исключение будет логироваться
              и поднято для обработки в вызывающем коде.

              Параметры:
              - locator: tuple, локатор искомого элемента в
                формате XPath (например, (By.XPATH, '//div[@id="element_id"]')).
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
            self.logger.debug(f"Элемент найден: {locator}")
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
             - locator: tuple, локатор искомых элементов в
               формате XPath (например, (By.XPATH, '//div[@class="element_class"]//div')).
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
            self.logger.debug(f"Элементы найдены: {locator}")
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

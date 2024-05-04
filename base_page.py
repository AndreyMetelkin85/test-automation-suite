from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC

from utils import highlight, highlights


class BasePage(ABC):
    """
        Базовый класс для страниц веб-сайта.

        Атрибуты:
            driver: Экземпляр веб-драйвера для управления браузером.
            base_url (str): Базовый URL-адрес сайта.
    """

    def __init__(self, driver):
        self.driver = driver
        self.stenn_url = "https://stenn.com/"
        self.demo_qa_url = 'https://demoqa.com/'

    @highlight
    def find_element(self, locator, time=10):
        """
            Метод для поиска одного элемента на странице.

            :param locator: Локатор элемента.
            :param time: Время ожидания (по умолчанию 10 секунд).
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @highlights
    def find_elements(self, locator, time=10):
        """
            Метод для поиска всех элементов на странице.

            :param locator: Локатор элементов.
            :param time: Время ожидания (по умолчанию 10 секунд).
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_element(self, element):
        """
            Прокручивает страницу к указанному элементу.
            :param element: Элемент, к которому нужно прокрутить страницу.
        """
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_web_site_stenn(self):
        """
            Метод для перехода на главную страницу сайта "https://stenn.com/".
        """
        return self.driver.get(self.stenn_url)

    def go_to_web_site_demo_qa(self):
        """
            Метод для перехода на главную страницу сайта 'https://demoqa.com/'.
        """
        return self.driver.get(self.demo_qa_url)

    def get_heading_label(self):
        """
            Абстрактный метод для получения заголовка страницы.
        """
        pass

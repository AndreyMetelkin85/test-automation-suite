from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class Wait(WebDriverWait):
    """
        Наследованный класс для ожидания элементов на веб-странице с использованием Selenium WebDriver.
        Добавляет пользовательские методы ожидания элементов.
    """

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def wait_until_the_url_is_visible(self, expected_url):
        """
            Ожидает, пока URL страницы не станет равным ожидаемому URL.
            :param expected_url: Ожидаемый URL.
        """
        return self.until(ES.url_to_be(expected_url))

    def wait_until_url_contains(self, expected_prefix):
        """
            Ожидает, пока URL страницы не будет содержать ожидаемый префикс.
            :param expected_prefix: Ожидаемый префикс URL.
        """
        return self.until(ES.url_contains(expected_prefix))

    def wait_until_the_element_is_visible(self, element):
        """
            Ожидает, пока элемент не станет видимым на странице.
            :param element: Элемент, который нужно дождаться.
        """
        return self.until(ES.visibility_of(element))

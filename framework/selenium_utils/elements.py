import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class BaseElement(WebElement):
    """
        Расширяет функциональность базового класса WebElement для работы с веб-элементами.

    """

    def __init__(self, element, element_locator, element_index=None):
        """
            Инициализирует экземпляр класса BaseElement.

            :param element: Элемент веб-страницы.
            :param element_locator: Локатор элемента.
            :param element_index: Индекс элемента (по умолчанию None).

        """
        super().__init__(element.parent, element.id)
        self.locator = element_locator
        self.element_index = element_index

        self.logger = logging.getLogger("TestLogger")

    def javascript_click(self):
        """
            Выполняет клик на элементе с использованием JavaScript.
        """
        self.parent.execute_script('arguments[0].scrollIntoView(); arguments[0].click()', self)

        # Логирование нажатия на элемент
        self.logger.debug('Нажать на элемент по локатору %s', self.locator)

    def mouse_hover(self):
        """
            Выполняет наведение мыши на элемент.
        """
        ActionChains(self.parent).move_to_element(self).perform()

        # Логирование наведения мыши на элемент
        self.logger.debug('Наведение мыши на элемент по локатору %s', self.locator)

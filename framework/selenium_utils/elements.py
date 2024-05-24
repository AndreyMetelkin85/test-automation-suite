import logging
import time
from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
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

    def appear_shadow(self, color: str):
        self.parent.execute_script(f"arguments[0].style.boxShadow = 'inset 0 0 0 3px {color}'", self)

    def delete_shadow(self):
        try:
            self.parent.execute_script(
                "const node = arguments[0]; setTimeout(function(){ node.style.boxShadow = ''; }"
                " , 1500)", self)
        except (TimeoutException, StaleElementReferenceException):
            pass

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

    def click(self, retries=5, element_backlight=True):
        """
            Попытаться выполнить клик по элементу на веб-странице.

            Аргументы:
            retries (int): Количество попыток выполнения клика в случае неудачи.
            element_backlight (bool): Флаг для включения/отключения подсветки элемента перед кликом и после него.

            Исключения:
            Raises:
                StaleElementReferenceException: Если ссылка на элемент устарела.
                ElementClickInterceptedException: Если другой элемент перекрывает целевой элемент и клик не может быть выполнен.

            Примечания:
            Notes:
                Перед выполнением клика элемент подсвечивается красным цветом для визуального подтверждения его обнаружения.
                Если клик не удается с первого раза из-за исключений, функция будет повторять попытки до указанного значения retries.
                Если параметр element_backlight установлен в True, элемент подсвечивается перед кликом и подсветка удаляется после клика.
        """
        for retry in range(retries):
            try:
                self.appear_shadow("red")

                if retry == 0:
                    super().click()
                    break

                if self.element_index:
                    super(BaseElement, self.parent.find_elements(self.__class__, self.locator))[
                        self.element_index].click()
                else:
                    super(BaseElement, self.find_element(self.__class__, self.locator)).click()

                break
            except (StaleElementReferenceException, ElementClickInterceptedException) as error:
                time.sleep(5)

                if retry == retries - 1:
                    raise error
        if element_backlight:
            try:
                self.delete_shadow()
            except (TimeoutException, StaleElementReferenceException):
                pass

        self.logger.debug('Нажать на элемент по локатору', self.locator)

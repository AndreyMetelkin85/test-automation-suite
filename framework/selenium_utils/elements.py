import logging
import time
from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException, ElementNotVisibleException
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
        self.parent.execute_script(f"arguments[0].style.boxShadow = 'inset 0 0 0 4px {color}'", self)

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

    def double_click(self):
        """
            Выполняет двойной клик по элементу.
        """
        ActionChains(self.parent).double_click(self).perform()

        self.logger.debug('Выполняется двойной клик по элементу с локатором: %s', self.locator)

    def right_click(self):
        """
            Выполняет клик правой кнопкой мыши по элементу.
        """
        ActionChains(self.parent).context_click(self).perform()

        self.logger.debug('Выполняется клик правой кнопкой по элементу с локатором: %s', self.locator)

    def click(self, retries=5, element_backlight=True):
        """
            Попытаться выполнить клик по элементу на веб-странице.

            Аргументы:
            retries (int): Количество попыток выполнения клика в случае неудачи.
            element_backlight (bool): Флаг для включения/отключения подсветки элемента перед кликом и после него.

            Исключения:
            Raises:
                StaleElementReferenceException: Если ссылка на элемент устарела.
                ElementClickInterceptedException: Если другой элемент перекрывает целевой элемент и клик не может
                быть выполнен.

            Примечания:
            Notes:
                Перед выполнением клика элемент подсвечивается красным цветом для визуального подтверждения
                его обнаружения.

                Если клик не удается с первого раза из-за исключений, функция будет повторять попытки до указанного
                значения retries.

                Если параметр element_backlight установлен в True, элемент подсвечивается перед кликом и подсветка
                удаляется после клика.
        """
        for retry in range(retries):
            try:
                self.appear_shadow("red")  # Подсветка элемента красным цветом для визуального подтверждения

                if retry == 0:
                    # Если это первая попытка, выполняем клик по элементу
                    super().click()
                    break

                if self.element_index:
                    # Если указан индекс элемента, выполняем клик по элементу с указанным индексом в найденных элементах
                    super(BaseElement, self.parent.find_elements(self.__class__, self.locator))[
                        self.element_index].click()
                else:
                    # Если индекс элемента не указан, выполняем клик по первому найденному элементу
                    super(BaseElement, self.find_element(self.__class__, self.locator)).click()
                break  # Выход из цикла, если клик прошел успешно

            except (StaleElementReferenceException, ElementClickInterceptedException) as error:
                time.sleep(5)

                if retry == retries - 1:
                    raise error

        if element_backlight:
            try:
                self.delete_shadow()  # Удаление подсветки элемента
            except (TimeoutException, StaleElementReferenceException):
                pass

        self.logger.debug('Нажать на элемент по локатору', self.locator)

    def get_text(self, retries=5):
        """
            Получить текстовое содержимое элемента на веб-странице.

            Аргументы:
            retries (int): Количество повторных попыток, в случае неудачи.

            Исключения:
            Raises:
                StaleElementReferenceException: Если ссылка на элемент устарела.

            Примечания:
            Notes:
                Перед выполнением попыток получения текста элемента он подсвечивается синим цветом для визуального
                подтверждения его обнаружения.
        """
        for retry in range(retries):
            try:
                self.appear_shadow("blue")  # Подсветка элемента синим цветом для визуального подтверждения

                if retry == 0:
                    # Если это первая попытка, удаляем подсветку и возвращаем текст элемента
                    self.delete_shadow()  # Удаление подсветки элемента
                    return self.text.strip()

                self.delete_shadow()  # Удаляем подсветку перед следующей попыткой

                if self.element_index:
                    # Если указан индекс элемента, получаем текст элемента по индексу в найденных элементах
                    return self.parent.find_elements(self.__class__, self.locator)[self.element_index].text.strip()
                else:
                    # Если индекс элемента не указан, получаем текст первого найденного элемента
                    return self.parent.find_element(self.__class__, self.locator).text.strip()

            except StaleElementReferenceException as error:
                time.sleep(5)

                if retry == retries - 1:
                    raise error  # Если достигнуто максимальное количество попыток, кидаем исключение

        self.logger.debug('Найти элемент по локатору', self.locator)

        return None

    def is_displayed(self, retries=5, element_backlight=True):
        """
            Проверить, виден ли элемент пользователю.

            Аргументы:
            retries (int): Количество повторных попыток, в случае неудачи.
            element_backlight (bool): Флаг для включения/отключения подсветки элемента перед проверкой и после нее.

            Исключения:
            Raises:
                StaleElementReferenceException: Если ссылка на элемент устарела.
                ElementNotInteractableException: Если элемент не взаимодействуемый.

            Примечания:
            Notes:
                Перед выполнением проверки видимости элемента он подсвечивается синим цветом для визуального
                подтверждения его обнаружения.
        """

        result = False  # Инициализация переменной для хранения результата проверки видимости элемента
        for retry in range(retries):
            try:

                self.appear_shadow("blue")  # Подсветка элемента синим цветом для визуального подтверждения

                if retry == 0:
                    result = super().is_displayed()  # Проверка видимости элемента в первой попытке
                    break

                if self.element_index:
                    # Если указан индекс элемента, проверяем видимость элемента по индексу в найденных элементах
                    result = super(BaseElement, self.parent.find_elements(self.__class__, self.locator))[
                        self.element_index].is_displayed()
                else:
                    # Если индекс элемента не указан, проверяем видимость первого найденного элемента
                    result = super(BaseElement, self.parent.find_element(self.__class__, self.locator)).is_displayed()
                break

            except (StaleElementReferenceException, ElementNotInteractableException) as error:
                time.sleep(5)

                if retry == retries - 1:
                    raise error  # Если достигнуто максимальное количество попыток, кидаем исключение

        if element_backlight:
            try:
                self.delete_shadow()  # Удаление подсветки элемента
            except (TimeoutException, StaleElementReferenceException, ElementNotVisibleException,
                    NoSuchElementException):
                pass

        self.logger.debug('Найти элемент по локатору', self.locator)
        return result

    def send_keys(self, keys, retries=5, element_backlight=True):
        """
            Имитирует ввод текста в элемент.
            Используется это для отправки простых событий нажатия клавиш или для заполнения полей формы

            Аргументы:
            keys (str): Строка символов, которые будут отправлены в элемент.
            retries (int): Количество попыток выполнения отправки клавиш в случае неудачи. По умолчанию 5.
            element_backlight (bool): Флаг для включения/отключения подсветки элемента перед отправкой клавиш и
            после него. По умолчанию True.

            Исключения:
            Raises:
                TimeoutException: Если выполнение операции занимает слишком много времени.
                NoSuchElementException: Если элемент не найден.
                ElementNotInteractableException: Если элемент не взаимодействуемый.

            Примечания:
            Перед отправкой клавиш элемент подсвечивается зеленым цветом для визуального подтверждения его обнаружения.

            Если отправка клавиш не удается с первого раза из-за исключений, функция будет повторять попытки
            до указанного значения retries.

            Если параметр element_backlight установлен в True, элемент подсвечивается перед отправкой клавиш
            и подсветка удаляется после отправки.
        """
        for retry in range(retries):
            try:
                self.appear_shadow("green")  # Подсветить элемент зеленым цветом для визуального подтверждения

                if retry == 0:
                    super().send_keys(keys)  # При первой удачной попытке передавать данные
                    break

                if self.element_index:
                    # Если задан индекс элемента, найти элементы и отправить клавиши в указанный элемент по индексу
                    super(BaseElement, self.parent.find_elements(self.__class__, self.locator))[
                        self.element_index].send_keys()

                    # Если индекс элемента не задан, найти элемент и отправить клавиши
                else:
                    super(BaseElement, self.parent.find_element(self.__class__, self.locator)).send_keys(keys)

                    break
            except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as error:
                time.sleep(5)  # Если произошла ошибка, подождать 5 секунд и повторить попытку

                if retry == -1:
                    raise error  # Если достигнуто максимальное количество попыток, выбросить исключение

        if element_backlight:
            self.delete_shadow()  # Удалить подсветку элемента, если включена подсветка

        self.logger.debug('Найти элемент по локатору', self.locator)

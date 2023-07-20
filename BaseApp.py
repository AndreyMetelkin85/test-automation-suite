from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def highlight(element):
    driver = element._parent
    driver.execute_script("arguments[0].style.border='5px solid blue'", element)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stenn.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


class Text:
    def __init__(self, element):
        self.element = element

    def is_displayed(self):
        return self.element.is_displayed()

    def text(self):
        return self.element.text


class Label:
    def __init__(self, element):
        self.element = element

    def is_displayed(self):
        return self.element.is_displayed()

    def text(self):
        return self.element.text

    def __getitem__(self, item):
        # Вернуть значение элемента, если поддерживается доступ по индексу (item)
        if hasattr(self.element, '__getitem__'):
            return self.element[item]
        else:
            raise TypeError("Element does not support indexing")


class Button:
    def __init__(self, element):
        self.element = element

    def click(self):
        self.element.click()

    def __getitem__(self, item):
        # Вернуть значение элемента, если поддерживается доступ по индексу (item)
        if hasattr(self.element, '__getitem__'):
            return self.element[item]
        else:
            raise TypeError("Element does not support indexing")

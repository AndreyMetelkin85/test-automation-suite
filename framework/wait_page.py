from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class Wait(WebDriverWait):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def wait_until_the_url_is_visible(self, expected_url):
        return self.until(ES.url_to_be(expected_url))

    def wait_until_url_contains(self, expected_prefix):
        return self.until(ES.url_contains(expected_prefix))

    def wait_until_the_element_is_visible(self, element):
        return self.until(ES.visibility_of(element))

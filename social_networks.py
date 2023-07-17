from selenium.webdriver.common.by import By

from elements import Button, Text


class SocialNetworks:
    pass


class SocialNetworks:
    def __init__(self, driver):
        self.driver = driver

    def social_networks(self) -> Button:
        return self.driver.find_elements(By.XPATH, '//div[@class="SocialGroup_SocialGroup_Icons___61mu"]/a')

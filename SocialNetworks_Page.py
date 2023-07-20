from selenium.webdriver.common.by import By
from BaseApp import Button, Text, BasePage


class SocialNetworks(BasePage):

    def social_networks(self) -> Button:
        return self.find_elements((By.XPATH, '//div[@class="SocialGroup_SocialGroup_Icons___61mu"]/a'))

    def footer_logo_sten(self) -> Text:
        return self.find_element((By.XPATH, '//*[@class="footer__contacts-logo"]'))

    def accept_all_pop_up_button(self) -> Button:
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))

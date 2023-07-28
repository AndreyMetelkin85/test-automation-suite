from selenium.webdriver.common.by import By
from base_page import BasePage


class SocialNetworks(BasePage):

    def social_networks(self):
        return self.find_elements((By.XPATH, '//div[@class="SocialGroup_SocialGroup_Icons___61mu"]/a'))

    def footer_logo_sten(self):
        return self.find_element((By.XPATH, '//*[@class="footer__contacts-logo"]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))

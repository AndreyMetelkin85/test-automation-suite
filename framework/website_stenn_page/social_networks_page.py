from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SocialNetworks(BasePage):

    def get_heading_label(self):
        pass

    def social_networks(self):
        return self.find_elements((By.XPATH, '//div[@class="social-media-icons"]//a'))

    def footer_logo_sten(self):
        return self.find_element((By.XPATH, '//a[@class="stenn-logo w-inline-block"]//img'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept all"]'))

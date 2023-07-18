from selenium.webdriver.common.by import By
from elements import Button, Text
from social_networks import SocialNetworks


class HeaderButtonsVerification:
    def __init__(self, driver):
        self.driver = driver

    def products_button(self) -> Button:
        return self.driver.find_element(By.XPATH, '//a[contains(text(), "Products")]')

    def solutions_button(self) -> Button:
        return self.driver.find_element(By.XPATH, '//a[contains(text(),"Solutions")]')

    def resources_button(self) -> Button:
        return self.driver.find_element(By.XPATH, '//a[contains(text(),"Resources")]')

    def contact_us_button(self) -> Button:
        return self.driver.find_element(By.XPATH, '//a[contains(text(),"Contact Us")]')

    def your_working_label(self) -> Text:
        return self.driver.find_element(By.XPATH, '//h1[text()="Your working capital platform"]')

    def boost_your_cash_label(self) -> Text:
        return self.driver.find_element(By.XPATH,
                                        '//div[text()="Boost your cash flow with streamlined invoice financing"]')

    def convert_your_invoices_label(self) -> Text:
        return self.driver.find_element(By.XPATH, '//div[text()="Convert your invoices "]')

    def articles_label(self) -> Text:
        return self.driver.find_element(By.XPATH, '//div[text()="Articles"]')

    def contact_us_label(self) -> Text:
        return self.driver.find_element(By.XPATH, '//div[text()="Contact Us"]')

    def accept_all_pop_up_button(self) -> Button:
        return self.driver.find_element(By.XPATH, '//*[@data-testid="ClearIcon"]')

    def footer_logo_stenn(self) -> Text:
        return self.driver.find_element(By.XPATH, '//*[@class="footer__contacts-logo"]')

    def get_social_networks(self) -> SocialNetworks:
        return SocialNetworks(self.driver)

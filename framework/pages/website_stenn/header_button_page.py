from selenium.webdriver.common.by import By
from base_page import BasePage


class HeaderButtons(BasePage):

    def get_heading_label(self):
        pass

    def products_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(), "Products")]'))

    def solutions_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Solutions")]'))

    def resources_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Resources")]'))

    def contact_us_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Contact Us")]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))

    def login_dropdown(self):
        return self.find_element((By.XPATH, '//div[text()="Log in"]'))

    def invoice_fincace_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "invoice-fincace"]'))

    def revenue_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "revenue"]'))

    def apply_for_finance_button(self):
        return self.find_element((By.XPATH, '//*[@id = "portal-apply-top-right"]'))

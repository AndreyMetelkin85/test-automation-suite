from selenium.webdriver.common.by import By
from base_page import BasePage


class HeaderButtons(BasePage):

    def get_heading_label(self):
        pass

    def products_button(self):
        return self.find_element((By.XPATH, '//div[@id="w-dropdown-toggle-6"]'))

    def financing_hover_button(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-6"]//a'))

    def solutions_button(self):
        return self.find_element((By.XPATH, '//div[@id="w-dropdown-toggle-7"]'))

    def solutions_hover_button(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-7"]//a'))

    def resources_button(self):
        return self.find_element((By.XPATH, '//div[@id="w-dropdown-toggle-8"]'))

    def resources_hover_button(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-8"]//a'))

    def resources_hover_button_right(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-8"]//following-sibling::div//a'))

    def contact_us_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Contact Us")]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept all"]'))

    def login_dropdown(self):
        return self.find_element((By.XPATH, '//div[text()="Log in"]'))

    def invoice_fincace_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "invoice-fincace"]'))

    def revenue_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "revenue"]'))

    def apply_for_finance_button(self):
        return self.find_element((By.XPATH, '//*[@id = "portal-apply-top-right"]'))

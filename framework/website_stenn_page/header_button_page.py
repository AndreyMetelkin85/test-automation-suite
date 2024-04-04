from selenium.webdriver.common.by import By
from base_page import BasePage


class HeaderButtons(BasePage):

    def get_heading_label(self):
        pass

    def products_button(self):
        return self.find_element((By.XPATH, '//div[text()="Products"]'))

    def financing_hover_button(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-0"]//a'))

    def solutions_button(self):
        return self.find_element((By.XPATH, '//div[text()="Solutions"]'))

    def solutions_hover_button(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-1"]//a'))

    def resources_button(self):
        return self.find_element((By.XPATH, '//div[text()="Resources"]'))

    def resources_hover_button(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-2"]//a'))

    # def resources_hover_button_right(self):
    #     return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-8"]//following-sibling::div//a'))

    def contact_us_button(self):
        return self.find_element((By.XPATH, '//a[contains(text(),"Contact Us")]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept all"]'))

    def login_button(self):
        return self.find_element((By.XPATH, '//div[text()="Log in"]'))

    def login_dropdown(self):
        return self.find_elements((By.XPATH, '//nav[@id="w-dropdown-list-5"]//child::a'))

    def invoice_fincace_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "invoice-fincace"]'))

    def revenue_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "revenue"]'))

    def apply_for_finance_button(self):
        return self.find_elements((By.XPATH, "(//a[contains(text(), 'Apply for Finance')])"))

    def partner_with_us_button(self):
        return self.find_element((By.XPATH, '//div[@class="div-block-109"]//a[text()="Partner With Us"]'))

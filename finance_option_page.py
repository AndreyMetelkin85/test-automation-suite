from selenium.webdriver.common.by import By
from base_page import BasePage


class FinanceOption(BasePage):
    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Select your finance option"]'))

    def international_and_domestic_label(self):
        return self.find_element((By.XPATH, '//h1[text()="International and Domestic Invoice Financing"]'))

    def revenue_based_financing_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Revenue-based Financing for your business"]'))

    def apply_for_finance_app(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "https://app.stenn.com/auth/sign-up"]'))

    def apply_for_finance_rbf(self):
        return self.find_element((By.XPATH, '//*[@data-testid = "https://rbf.stenn.com/auth/sign-up"]'))

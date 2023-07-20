from selenium.webdriver.common.by import By
from BaseApp import Button, Text, Label, BasePage


class InvoiceFinancing(BasePage):

    def heading_convert_your_invoices_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="Convert your invoices "]'))

    def accept_all_pop_up_button(self) -> Button:
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))

    def is_displayed(self):
        pass

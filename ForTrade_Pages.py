from selenium.webdriver.common.by import By
from BaseApp import Button, Text, Label, BasePage


class ForTrade(BasePage):

    def heading_boost_your_cash_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="Boost your cash flow with streamlined invoice financing"]'))

    def accept_all_pop_up_button(self) -> Button:
        return self.find_element((By.XPATH, '//*[text()="Accept All"]'))

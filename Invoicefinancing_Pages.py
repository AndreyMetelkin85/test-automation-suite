from selenium.webdriver.common.by import By
from BaseApp import Button, Text, Label, BasePage


class InvoiceFinancing(BasePage):
    def sign_up_heading_convert_your_label(self) -> Text:
        return self.find_element((By.XPATH, '//h1[contains(.,"Convert your invoices")]'))

    def heading_convert_your_invoices_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="Convert your invoices "]'))

    def apply_for_finance_button(self) -> Button:
        return self.find_elements((By.XPATH, '(//span[text()="Apply for finance"])'))

    def learn_more_button(self) -> Button:
        return self.find_element((By.XPATH, '//span[text()="Learn more"]'))

    def stenn_named_label(self) -> Label:
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

    def asked_questions_button(self) -> Button:
        return self.find_elements((By.XPATH, '(//p[@class="styles_questionLinkAccordionTitle___aB8Q"])'))

    def how_it_works_label(self) -> Text:
        return self.find_element((By.XPATH, '//p[contains(., "If you have any invoices waiting")]'))

    def almost_any_company_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="More About Applicants"]'))

    def six_benefits_label(self) -> Text:
        return self.find_element((By.XPATH, '//div[text()="You as an importer..."]'))

    def we_finance_label(self) -> Text:
        return self.find_elements((By.XPATH, '//*[@class="cost-calc__bottom-half-suppliers"]//*'))

    def close_live_chat_button(self) -> Button:
        return self.find_element((By.XPATH, '//*[@class="conversations-visitor-close-icon"]'))

    def is_displayed(self):
        pass

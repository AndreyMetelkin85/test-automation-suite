from selenium.webdriver.common.by import By
from base_page import BasePage


class InvoiceFinancing(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[contains(.,"Convert your invoices")]'))

    def apply_for_finance_button(self):
        return self.find_elements((By.XPATH, '(//a[text()="Apply for finance"])'))

    def stenn_named_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

    def asked_questions_button(self):
        return self.find_elements((By.XPATH, '//div[@class="faq1_accordion-2"]'))

    def how_it_works_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "If you have any invoices waiting")]'))

    def almost_any_company_label(self):
        return self.find_element((By.XPATH, '//h1[text()="More About Applicants"]'))

    def six_benefits_label(self):
        return self.find_element((By.XPATH, '//p[text()="You as an importer..."]'))

    def stenn_pricing_information(self):
        return self.find_element((By.XPATH, '//div[@class="text-block-47"]'))

    def close_live_chat_button(self):
        return self.find_element((By.XPATH, '//*[@class="conversations-visitor-close-icon"]'))

    def how_it_works_button(self):
        return self.find_element((By.XPATH, '//div[text()="How it works: Get financed in 48h, all online"]'))

    def almost_any_company_button(self):
        return self.find_element((By.XPATH, '//div[text()="Almost any company"]'))

    def six_benefits_of_stenn_financing_button(self):
        return self.find_element((By.XPATH, '//div[text()="Six benefits of Stenn financing"]'))

    def fees_starting_button(self):
        return self.find_element((By.XPATH, '//div[text()="Fees starting from 0.7% per invoice"]'))

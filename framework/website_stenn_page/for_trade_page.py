from selenium.webdriver.common.by import By
from base_page import BasePage


class ForTrade(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Boost your cash flow with streamlined invoice financing"]'))

    def apply_for_finance_button(self):
        return self.find_element((By.XPATH, '//a[text()="Apply for finance"]'))

    def frequently_asked_questions_button(self):
        return self.find_elements((By.XPATH, '//div[@class="faq1_accordion-2"]'))

    def how_it_works_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "If you have any invoices waiting")]'))

    def almost_any_company_label(self):
        return self.find_element((By.XPATH, '//h1[text()="More About Applicants"]'))

    def six_benefits_label(self):
        return self.find_element((By.XPATH, '//div[text()="Six benefits of Stenn financing"]'))

    def we_finance_label(self):
        return self.find_elements((By.XPATH, '//*[@class="cost-calc__bottom-half-suppliers"]//*'))

    def learn_more_button(self):
        return self.find_element((By.XPATH, '//a[text()="Learn more"]'))

    def read_news_button(self):
        return self.find_element((By.XPATH, '//a[text()="Read all News"]'))

    def convert_your_invoices_label(self):
        return self.find_element((By.XPATH, '//h1[contains(.,"Convert your invoices")]'))

    def apply_for_finance(self):
        return self.find_element((By.XPATH, '//a[text()="Apply for Finance"]'))

    def learn_more_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

    def how_it_works_button(self):
        return self.find_element((By.XPATH, '//div[text()="How it works: Get financed in 48h, all online"]'))

    def almost_any_company_button(self):
        return self.find_element((By.XPATH, '//div[text()="Almost any company"]'))

    def six_benefits_of_stenn_financing_button(self):
        return self.find_element((By.XPATH, '//div[text()="Six benefits of Stenn financing"]'))

    def fees_starting_button(self):
        return self.find_element((By.XPATH, '//div[text()="Fees starting from 0.7% per invoice"]'))

from selenium.webdriver.common.by import By
from base_page import BasePage


class ForTrade(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Boost your cash flow with streamlined invoice financing"]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept all"]'))

    def apply_for_finance_button(self):
        return self.find_element((By.XPATH, '//span[text()="Apply for finance"]'))

    def frequently_asked_questions_button(self):
        return self.find_elements((By.XPATH, '(//p[@class="styles_questionLinkAccordionTitle___aB8Q"])'))

    def how_it_works_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "If you have any invoices waiting")]'))

    def almost_any_company_label(self):
        return self.find_element((By.XPATH, '//div[text()="More About Applicants"]'))

    def six_benefits_label(self):
        return self.find_element((By.XPATH, '//div[text()="You as an importer..."]'))

    def we_finance_label(self):
        return self.find_elements((By.XPATH, '//*[@class="cost-calc__bottom-half-suppliers"]//*'))

    def learn_more_button(self):
        return self.find_element((By.XPATH, '//span[text()="Learn more"]'))

    def read_news_button(self):
        return self.find_element((By.XPATH, '//span[text()="Read all News"]'))

    def convert_your_invoices_label(self):
        return self.find_element((By.XPATH, '//h1[contains(.,"Convert your invoices")]'))

    def apply_for_finance(self):
        return self.find_element((By.XPATH, '//span[text()="Apply for Finance"]'))

    def learn_more_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

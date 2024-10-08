from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Your working capital platform"]'))

    def apply_for_finance_button(self):
        return self.find_elements((By.XPATH, '(//a[@class="button w-button" and text()="Apply for Finance"])'))

    def right_for_you(self):
        return self.find_element((By.XPATH, '//div[text()="Choose, What’s Right For You?"]'))

    def invoice_financing_label(self):
        return self.find_element((By.XPATH, '//h1[text()="International and Domestic Invoice Financing"]'))

    def revenue_based_financing_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Revenue-based Financing for your business"]'))

    def e_commerce_label(self):
        return self.find_element((By.XPATH, '//h1[text()="E-commerce"]'))

    def saas_label(self):
        return self.find_element((By.XPATH, '//h1[text()="SaaS"]'))

    def convert_your_invoices_label(self):
        return self.find_element((By.XPATH, '//h1[contains(.,"Convert your invoices")]'))

    def looking_financing_label(self):
        return self.find_element((By.XPATH,
                                  '//div[text()="Looking for a financing solution that helps your SaaS business grow?"]'))

    def what_stenn_label(self):
        return self.find_elements((By.XPATH, '//div[@class="w-layout-grid layout364_row-2"]/descendant::h3'))

    def what_stenn_button(self):
        return self.find_elements((By.XPATH, '//div[@class="w-layout-grid layout364_row-2"]/descendant::a'))

    def useful_guides_label(self):
        return self.find_element((By.XPATH, '//p[text()="Useful Guides"]'))

    def join_stenn_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Join Stenn"]'))

    def questions_answers_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Questions & Answers"]'))

    def read_news_button(self):
        return self.find_element((By.XPATH, '//a[text()="Read all News"]'))

    def apply_online_button(self):
        return self.find_element((By.XPATH, '//span[text()="Apply online"]'))

    def accept_all_pop_up_button(self):
        return self.find_element((By.XPATH, '//*[text()="Accept all"]'))

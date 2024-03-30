from selenium.webdriver.common.by import By
from base_page import BasePage


class RevenueBasedFinancing(BasePage):

    def revenue_based_financing_button(self):
        return self.find_element((By.XPATH, '//a[text()="Revenue-Based Financing"]'))

    def get_heading_label(self):
        return self.find_element((By.XPATH,
                        '//h1[text()="Are you an E-commerce or SaaS business looking for a financing solution?"]'))

    def check_my_limit_button(self):
        return self.find_element((By.XPATH, '//a[text()="Check my limit"]'))

    def apply_for_finance_button(self):
        return self.find_elements((By.XPATH, '(//a[text()="Apply for finance"])'))

    def flexible_financing_options_label(self):
        return self.find_element((By.XPATH, '//h2[text()="Flexible Financing Options"]'))

    def unlock_e_commerce_label(self):
        return self.find_element((By.XPATH, '//h2[text()="Unlock E-Commerce Potential with Revenue-Based Financing"]'))

    def drive_saas_growth_label(self):
        return self.find_element((By.XPATH, '//h2[text()="Drive SaaS Growth with Recurring Revenue Financing"]'))

    def stenn_named_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

    def learn_more_button(self):
        return self.find_element((By.XPATH, '//span[text()="Learn more"]'))

    def frequently_asked_questions(self):
        return self.find_elements((By.XPATH, '//div[@class="faq1_accordion-2"]'))

    def revenue_based_financing_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "Revenue based financing")]'))

    def typically_our_customers_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "Typically, our customers")]'))

    def repayments_for_your_draw_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "Repayments for your draw")]'))

    def in_order_to_accurately_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "In order to accurately")]'))

    def sten_is_uk_label(self):
        return self.find_element((By.XPATH, '//p[contains(., "Stenn is a UK")]'))

    def read_news_button(self):
        return self.find_element((By.XPATH, '//a[text()="Read all News"]'))

    def what_is_revenue_button(self):
        return self.find_element((By.XPATH, '//div[text()="What is Revenue-Based Financing?"]'))

    def what_can_i_use_button(self):
        return self.find_element((By.XPATH, '//div[text()="What can I use the funds for?"]'))

    def how_do_repayments_work_button(self):
        return self.find_element((By.XPATH, '//div[text()="How do repayments work?"]'))

    def what_information_do_button(self):
        return self.find_element((By.XPATH, '//div[text()="What information do I need to provide?"]'))

    def who_is_stenn(self):
        return self.find_element((By.XPATH, '//div[text()="Who is Stenn?"]'))

from selenium.webdriver.common.by import By
from base_page import BasePage


class ForECommerce(BasePage):

    def ecommerce_batton(self):
        return self.find_element((By.XPATH, '//a[@class="styles_tabsTab__2bOpf"]'))

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//div[@class="styles_blockTextWrapper__jxmTm"]'))

    def check_my_limit_button(self):
        return self.find_element((By.XPATH, '//span[text()="Check my limit"]'))

    def learn_more_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

    def learn_more_button(self):
        return self.find_element((By.XPATH, '//span[text()="Learn more"]'))

    def frequently_asked_questions(self):
        return self.find_elements((By.XPATH, '(//p[@class="styles_questionLinkAccordionTitle___aB8Q"])'))

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
        return self.find_element((By.XPATH, '//span[text()="Read all News"]'))

    def learn_more_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

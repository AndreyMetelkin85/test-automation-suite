from base_page import BasePage
from selenium.webdriver.common.by import By


class Saas(BasePage):

    def saas_button(self):
        return self.find_elements((By.XPATH, '//div[@class= "styles_tabsWrapper__xUv97"]//a'))

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//div[@class= "header84_card-content-top"]'))

    def privacy_policy_button(self):
        return self.find_element((By.XPATH, '//div[@class="text-block-43"]//a'))

    def privacy_policy_label(self):
        return self.find_element((By.XPATH, '//h2[text()="STENN INTERNATIONAL LTD"]'))

    def contact_us_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Contact Us"]'))

    def join_the_beta_button(self):
        return self.find_element((By.XPATH, '//a[text()="Join the beta"]'))

    def learn_more_button(self):
        return self.find_element((By.XPATH, '//a[text()="Learn more"]'))

    def learn_more_label(self):
        return self.find_element((By.XPATH, '//h1[contains(., "Stenn named")]'))

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

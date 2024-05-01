from selenium.webdriver.common.by import By

from base_page import BasePage


class ElementsPage(BasePage):

    def text_box_label(self):
        return self.find_element((By.XPATH, '//h1[@class="text-center" and text()="Text Box"]'))

    def user_name_input(self):
        return self.find_element((By.XPATH, '//input[@id="userName"]'))

    def user_email_input(self):
        return self.find_element((By.XPATH, '//input[@id="userEmail"]'))

    def current_address_input(self):
        return self.find_element((By.XPATH, '//textarea[@id="currentAddress"]'))

    def permanent_address_input(self):
        return self.find_element((By.XPATH, '//textarea[@id="permanentAddress"]'))

    def submit_button(self):
        return self.find_element((By.XPATH, '//button[@id="submit"]'))

    def output_field(self):
        return self.find_elements((By.XPATH, '//div[@id="output"]//descendant::p'))

    def check_box_label(self):
        return self.find_element((By.XPATH, '//h1[@class="text-center" and text()="Check Box"]'))

    def expand_all_button(self):
        return self.find_element((By.XPATH, '//button[@class="rct-option rct-option-expand-all" and @type="button"]'))

    def collapse_all_button(self):
        return self.find_element((By.XPATH, '//button[@class="rct-option rct-option-collapse-all" and @type="button"]'))

    def home_title(self):
        return self.find_element((By.XPATH, '//span[@class="rct-title" and text()="Home"]'))

    def you_have_selected_results(self):
        return self.find_element((By.XPATH, '//div[@id="result"]'))

    def dropdown_arrow_home_button(self):
        return self.find_element((By.XPATH, '//div[@id="tree-node"]/descendant::button'))


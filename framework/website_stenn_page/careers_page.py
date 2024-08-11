from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Careers(BasePage):
    def get_heading_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Join Stenn"]'))

    def view_openings_button(self):
        return self.find_elements((By.XPATH, '(//span[text()="View Openings"])'))

    def why_join_stenn(self):
        return self.find_element((By.XPATH, '//h1[text()="Why Join Stenn?"]'))

    def why_join_stenn_subheadings(self):
        return self.find_elements((By.XPATH, '//div[@class="Careers_reasons__6jWsZ"]/descendant::h2'))

    def making_difference_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Making a difference"]'))

    def culture_belonging_label(self):
        return self.find_element((By.XPATH, '//div[text()="A Culture of Belonging"]'))

    def life_at_stenn_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Life at Stenn"]'))

    def leadership_team_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Meet the Leadership Team"]'))

    def our_values_guide_label(self):
        return self.find_element((By.XPATH, '//h1[text()="Our Values Guide Everything We Do"]'))

    def our_values_guide_subheadings(self):
        return self.find_elements((By.XPATH, '//div[@class="Careers_allValuesWrapper__QIOKf"]/descendant::h2'))

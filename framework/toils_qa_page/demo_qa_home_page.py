from selenium.webdriver.common.by import By
from base_page import BasePage


class ToolsQaHome(BasePage):

    def tools_qa_label(self):
        return self.find_element((By.XPATH, '//*[@id="app"]/header//a'))

    def category_cards_home_page(self):
        return self.find_elements((By.XPATH, '//div[@class="home-content"]/child::div[2]/div/div'))

    def left_panel_buttons(self):
        return self.find_elements((By.XPATH, '//div[@class="element-list collapse show"]//descendant::li'))

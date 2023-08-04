from selenium.webdriver.common.by import By
from base_page import BasePage


class Resources(BasePage):

    def list_title_buttons(self):
        return self.find_elements((By.XPATH, '//div[@class="styles_tabs__WdiyN"]//a'))

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//div[text()="Articles"]'))

    def blog_titles_buttons(self):
        return self.find_elements((By.XPATH, '//div[@class="styles_blogTabs__hRljt"]//a'))

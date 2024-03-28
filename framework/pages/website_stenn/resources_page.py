from abc import ABC
from selenium.webdriver.common.by import By
from base_page import BasePage


class Resources(BasePage):

    def get_heading_label(self):
        return self.find_element((By.XPATH, '//div[text()="Articles"]'))

    def list_resource_buttons(self):
        return self.find_elements((By.XPATH, '//div[@class="nav-container res-container"]//a'))

    def get_articles_heading_label(self):
        return self.find_element((By.XPATH, '//div[text()="Articles"]'))

    def list_blog_post_titles(self):
        return self.find_elements((By.XPATH, '//div[@class="styles_blogTabs__hRljt"]//a'))

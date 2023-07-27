from selenium.webdriver.common.by import By
from BaseApp import Button, Text, Label, BasePage, Input, Dropdown


class MailRu(BasePage):

    def create_mail_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid="mailbox-create-link"]'))

    def come_in_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid="enter-mail-primary"]'))

    def logo_label(self):
        return self.find_element((By.XPATH, '//*[@data-testid="logo-item"]'))

    def create_mailbox_label(self):
        return self.find_element((By.XPATH, '//*[@data-testid="first-step-header"]'))

    def first_name_input(self) :
        return self.find_element((By.XPATH, '//*[@data-testid="first-name"]'))

    def last_name_input(self):
        return self.find_element((By.XPATH, '//*[@data-testid="last-name"]'))

    def birth_date(self):
        return self.find_element((By.XPATH, '//*[@data-testid="birth-date__day"]'))

    def birth_date_month(self):
        return self.find_element((By.XPATH, '//*[@data-testid="birth-date__month"]'))

    def birth_date_year(self):
        return self.find_element((By.XPATH, '//*[@data-testid="birth-date__year"]'))

    def name_of_box_input(self):
        return self.find_element((By.XPATH, '//*[@data-testid="account__input"]'))

    def password_input(self):
        return self.find_element((By.XPATH, '//*[@data-testid="password-input"]'))

    def password_again_input(self):
        return self.find_element((By.XPATH, '//*[@data-testid="password-confirm-input"]'))

    def phone_number_input(self):
        return self.find_element((By.XPATH, '//*[@data-testid="phone-input"]'))

    def create_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid="first-step-submit"]'))

    def recaptcha_box(self):
        return self.find_element((By.XPATH, '//*[@id="recaptcha-anchor"]'))

    def continue_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid="verification-next-button"]'))

    def step_header_code_label(self):
        return self.find_element((By.XPATH, '//*[@data-testid="verification-step-header-code"]'))

    def enter_mail_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid="enter-mail-primary"]'))

    def header_text_label(self):
        return self.find_element((By.XPATH, '//*[@data-testid="header-text"]'))

    def username_input(self):
        return self.find_element((By.XPATH, '//*[@name="username"]'))

    def domain_select(self):
        return self.find_element((By.XPATH, '//*[@data-testid="domain-select-value:inbox.ru"]'))

    def next_button(self):
        return self.find_element((By.XPATH, '//*[@data-testid="next-button"]'))

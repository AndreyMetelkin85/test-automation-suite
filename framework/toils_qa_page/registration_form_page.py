from selenium.webdriver.common.by import By

from base_page import BasePage


class RegistrationForm(BasePage):

    def registration_form_label(self):
        return self.find_element((By.XPATH, '//div[@id="registration-form-modal"]'))

    def first_name(self):
        return self.find_element((By.XPATH, '//div[@id="firstName-wrapper"]/descendant::input'))

    def last_name(self):
        return self.find_element((By.XPATH, '//div[@id="lastName-wrapper"]/descendant::input'))

    def email(self):
        return self.find_element((By.XPATH, '//div[@id="userEmail-wrapper"]/descendant::input'))

    def age(self):
        return self.find_element((By.XPATH, '//div[@id="age-wrapper"]/descendant::input'))

    def salary(self):
        return self.find_element((By.XPATH, '//div[@id="salary-wrapper"]/descendant::input'))

    def department(self):
        return self.find_element((By.XPATH, '//div[@id="department-wrapper"]/descendant::input'))

    def submit_button(self):
        return self.find_element((By.XPATH, '//button[@id="submit"]'))

    def fill_form_and_submit(self, first_name, last_name, email, age, salary, department):
        self.first_name().send_keys(first_name)
        self.last_name().send_keys(last_name)
        self.email().send_keys(email)
        self.age().send_keys(age)
        self.salary().send_keys(salary)
        self.department().send_keys(department)
        self.submit_button().click()

from selenium.webdriver.common.by import By

from base_page import BasePage


class PracticeForm(BasePage):

    def practice_form_label(self):
        return self.find_element((By.XPATH, '//h1[@class="text-center" and text()="Practice Form"]'))

    def student_registration_form_label(self):
        return self.find_element((By.XPATH, '//h5[text()="Student Registration Form"]'))

    def first_name_input(self):
        return self.find_element((By.XPATH, '//input[@id="firstName"]'))

    def last_name_input(self):
        return self.find_element((By.XPATH, '//input[@id="lastName"]'))

    def user_email_input(self):
        return self.find_element((By.XPATH, '//input[@id="userEmail"]'))

    def gender_input(self):
        return self.find_elements((By.XPATH, '//div[@id="genterWrapper"]//descendant::div//div'))

    def mobile_number_input(self):
        return self.find_element((By.XPATH, '//input[@id="userNumber"]'))

    def birth_date_input(self):
        return self.find_element((By.XPATH, '//input[@id="dateOfBirthInput"]'))

    def subjects_input(self):
        return self.find_element((By.XPATH, '//div[@id="subjectsContainer"]'))

    def hobbies_input(self):
        return self.find_elements((By.XPATH, '//div[@id="hobbiesWrapper"]//descendant::div/div'))

    def upload_picture(self):
        return self.find_element((By.XPATH, '//input[@id="uploadPicture"]'))

    def current_address_input(self):
        return self.find_element((By.XPATH, '//textarea[@id="currentAddress"]'))

    def state_dropdown(self):
        return self.find_element((By.XPATH, '//div[@id="state"]'))

    def city_dropdown(self):
        return self.find_element((By.XPATH, '//div[@id="city"]'))

    def submit_button(self):
        return self.find_element((By.XPATH, '//button[@id="submit"]'))

    def result_submitting_label(self):
        return self.find_element((By.XPATH, '//div[@id="example-modal-sizes-title-lg"]'))

    def result_submitting_form(self):
        return self.find_element((By.XPATH, '//div[@class="table-responsive"]//child::tr'))

from selenium.webdriver.common.by import By
from framework.page_fixture import RegistrationForm
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

    def radio_button_yes(self):
        return self.find_element((By.XPATH, '//input[@id="yesRadio"]'))

    def radio_button_impressive(self):
        return self.find_element((By.XPATH, '//input[@id="impressiveRadio"]'))

    def selected_result(self):
        return self.find_element((By.XPATH, '//p[@class="mt-3"]'))

    def add_button(self):
        return self.find_element((By.XPATH, '//button[@id="addNewRecordButton"]')).click()

    def click_add_button_and_open_registration_form(self):
        self.add_button().click()
        return RegistrationForm(self.driver)

    def results_table(self):
        return self.find_elements((By.XPATH, '//div[@class="rt-tbody"]/div/div'))

    def update_data_button(self):
        return self.find_elements(
            (By.XPATH, '//div[@class="ReactTable -striped -highlight"]/descendant::span[@class="mr-2"]'))

    def delete_user(self):
        return self.find_elements(
            (By.XPATH, '//div[@class="ReactTable -striped -highlight"]/descendant::span[@title="Delete"]'))

    def double_click_button(self):
        return self.find_element((By.XPATH, '//button[@id="doubleClickBtn"]'))

    def right_click_button(self):
        return self.find_element((By.XPATH, '//button[@id="rightClickBtn"]'))

    def click_me_button(self):
        return self.find_element((By.XPATH, '//button[text()="Click Me"]'))

    def results_button_click(self):
        return self.find_elements((By.XPATH, '//div[@class="col-12 mt-4 col-md-6"]/descendant::p'))

    def open_new_tab_home_page(self):
        return self.find_element((By.XPATH, '//a[@id="simpleLink"]'))

    def open_new_tab_dynamic_link_home_page(self):
        return self.find_element((By.XPATH, '//a[@id="dynamicLink"]'))

    def created_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="created"]'))

    def no_content_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="no-content"]'))

    def moved_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="moved"]'))

    def bad_request_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="bad-request"]'))

    def unauthorized_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="unauthorized"]'))

    def forbidden_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="forbidden"]'))

    def invalid_url_send_api_call(self):
        return self.find_element((By.XPATH, '//a[@id="invalid-url"]'))

    def response_text(self):
        return self.find_elements((By.XPATH, '//p[@id="linkResponse"]'))

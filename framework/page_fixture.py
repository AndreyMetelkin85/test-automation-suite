from base.base_page import BasePage
from pages.practice_form_page import PracticeForm
from pages.forms_page.registration_form_page import RegistrationForm
from pages.demo_qa_home_page import ToolsQaHome
from pages.elements_page import ElementsPage


class PageFixture:
    """
        Класс для создания фикстуры страниц, которая предоставляет доступ к объектам страниц сайта.
    """
    def __init__(self, driver):

        self.demo_qa_home_page = ToolsQaHome(driver)
        self.elements_page = ElementsPage(driver)
        self.go_to_web_site_demo_qa = BasePage(driver)
        self.registration_form = RegistrationForm(driver)
        self.practice_form = PracticeForm(driver)

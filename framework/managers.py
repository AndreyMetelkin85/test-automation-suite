from base.base_page import BasePage
from pages.practice_form_page import PracticeForm
from pages.forms_page.registration_form_page import RegistrationForm
from pages.demo_qa_home_page import ToolsQaHome
from pages.elements_page import ElementsPage
from api_methods.petstore_pet_method import PetStorePet
from api_methods.petstore_order_method import PetStoreOrder
from api_methods.petstore_user_method import PetStoreUser


class PageManager:
    """ Класс для управления страницами веб-приложения.  """

    def __init__(self, driver):
        self.demo_qa_home_page = ToolsQaHome(driver)
        self.elements_page = ElementsPage(driver)
        self.go_to_web_site_demo_qa = BasePage(driver)
        self.registration_form = RegistrationForm(driver)
        self.practice_form = PracticeForm(driver)


class ApiManager:
    """ Класс для управления API методами приложения. """

    def __init__(self):
        self.pet_store_pet = PetStorePet()
        self.pet_store_order = PetStoreOrder()
        self.pet_store_user = PetStoreUser()

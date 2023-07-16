import time

from selenium.webdriver.common.action_chains import ActionChains
from headerbuttonsverification_page import HeaderButtonsVerification
from config import highlight
from fixtures import driver


def test_buttons_in_header(driver):
    home_page = HeaderButtonsVerification(driver)
    products_label = home_page.your_working_label()
    assert products_label.text == "Your working capital platform"
    highlight(products_label)

    products_button = home_page.products_button()
    products_button.click()
    time.sleep(1)

    convert_label = home_page.convert_your_invoices_label()
    assert convert_label.text == "Convert your invoices\ninto cash long before\nthe due date"
    highlight(convert_label)

    solutions_button = home_page.solutions_button()
    solutions_button.click()
    time.sleep(1)

    solutions_label = home_page.boost_your_cash_label()
    assert solutions_label.text == "Boost your cash flow with streamlined invoice financing"
    highlight(solutions_label)

    resources_button = home_page.resources_button()
    resources_button.click()
    time.sleep(1)

    resources_label = home_page.articles_label()
    assert resources_label.text == "Articles"
    highlight(resources_label)

    contact_us_button = home_page.contact_us_button()
    contact_us_button.click()
    time.sleep(1)

    contact_us_label = home_page.contact_us_label()
    assert contact_us_label.text == "Contact Us"
    highlight(contact_us_label)


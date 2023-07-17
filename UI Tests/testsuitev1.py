import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from headerbuttonsverification_page import HeaderButtonsVerification
from config import highlight
from fixtures import driver, slow_scroll
from social_networks import SocialNetworks


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


def test_opening_social_networks(driver, slow_scroll):
    home_page = HeaderButtonsVerification(driver)
    pop_up_button = home_page.pop_up_close_button()
    pop_up_button.click()

    slow_scroll(driver, scroll_step=100, pause_duration=0.1)

    footer_logo = home_page.footer_logo_stenn()
    assert footer_logo.is_displayed()
    highlight(footer_logo)

    linkedin_button = home_page.get_social_networks()
    linkedin_button.social_networks()[0].click()
    time.sleep(3)

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://www.linkedin.com/company/stenn-financial-services?original_referer="
    assert current_url == expected_url

    driver.switch_to.window(current_window)

    facebook_button = home_page.get_social_networks()
    facebook_button.social_networks()[2].click()
    time.sleep(3)

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://www.facebook.com/StennIntl"
    assert current_url == expected_url

    driver.switch_to.window(current_window)

    twitter_button = home_page.get_social_networks()
    twitter_button.social_networks()[1].click()
    time.sleep(3)

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://twitter.com/i/flow/login?redirect_after_login=%2FStenn_Intl"
    assert current_url == expected_url

    driver.switch_to.window(current_window)

    youtube_button = home_page.get_social_networks()
    youtube_button.social_networks()[3].click()
    time.sleep(3)

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://www.youtube.com/channel/UCVsztAj0QmhKkfu4IKMHUOA"
    assert current_url == expected_url

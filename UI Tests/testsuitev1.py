import time
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from headerbuttonsverification_page import HeaderButtonsVerification
from config import highlight
from fixtures import driver, slow_scroll
from social_networks import SocialNetworks
from HomePage import HomePage


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

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

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
    expected_url = "https://www.linkedin.com/company/stenn-financial-services"
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

    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://www.youtube.com/channel/UCVsztAj0QmhKkfu4IKMHUOA"
    assert current_url == expected_url


def test_сlick_and_transitions_home_page(driver, slow_scroll):
    home_page = HeaderButtonsVerification(driver)
    products_label = home_page.your_working_label()
    assert products_label.text == "Your working capital platform"
    highlight(products_label)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    page_open = HomePage(driver)
    app_for_finance_button = page_open.apply_for_finance_button_1()
    app_for_finance_button.click()
    time.sleep(1)

    right_for_you_label = page_open.right_for_you()
    assert right_for_you_label.is_displayed()
    highlight(right_for_you_label)

    driver.back()
    time.sleep(1)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    list_buttons = page_open.navi_bar_button()
    list_buttons[0].click()
    time.sleep(1)

    invoice_financing_label = page_open.invoice_financing_label()
    assert invoice_financing_label.is_displayed()
    highlight(invoice_financing_label)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    apply_finance_button = page_open.apply_for_finance_button_2()
    apply_finance_button.click()
    time.sleep(1)

    convert_your_invoices = page_open.convert_your_invoices_label()
    assert convert_your_invoices.is_displayed()
    highlight(convert_your_invoices)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    list_buttons = page_open.navi_bar_button()
    list_buttons[1].click()
    time.sleep(1)

    e_commerce_label = page_open.e_commerce_label()
    assert e_commerce_label.is_displayed()
    highlight(e_commerce_label)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    e_commerce_button = page_open.apply_for_finance_button_2()
    e_commerce_button.click()
    time.sleep(1)

    current_url = driver.current_url
    expected_url = "https://rbf.stenn.com/auth/sign-up"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    list_buttons = page_open.navi_bar_button()
    list_buttons[2].click()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    saas_label = page_open.saas_label()
    assert saas_label.is_displayed()
    highlight(saas_label)

    apply_finance_saas_button = page_open.apply_for_finance_button_2()
    apply_finance_saas_button.click()
    time.sleep(1)

    financing_solution_label = page_open.looking_financing_label()
    assert financing_solution_label.is_displayed()

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    driver.execute_script("window.scrollBy(0, 1200);")
    time.sleep(2)

    articles_label = page_open.what_stenn_label()
    assert articles_label[0].is_displayed()
    highlight(articles_label[0])

    articles_read_more_button = page_open.what_stenn_button()
    articles_read_more_button[0].click()
    time.sleep(1)

    articles_label = home_page.articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    useful_guides_label = page_open.what_stenn_label()
    assert useful_guides_label[1].is_displayed()
    highlight(useful_guides_label[1])

    driver.execute_script("window.scrollBy(0, 1800);")
    time.sleep(2)
    useful_guides_button = page_open.what_stenn_button()
    useful_guides_button[1].click()
    time.sleep(1)

    useful_guides_label = page_open.useful_guides_label()
    assert useful_guides_label.is_displayed()
    highlight(useful_guides_label)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    careers_label = page_open.what_stenn_label()
    assert careers_label[2].is_displayed()
    highlight(careers_label[2])

    careers_button = page_open.what_stenn_button()
    careers_button[2].click()
    time.sleep(1)

    careers_label = page_open.join_stenn_label()
    assert careers_label.is_displayed()
    highlight(careers_label)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    faq_label = page_open.what_stenn_label()
    assert faq_label[3].is_displayed()
    highlight(faq_label[3])

    faq_button = page_open.what_stenn_button()
    faq_button[3].click()
    time.sleep(1)

    faq_label = page_open.questions_answers_label()
    assert faq_label.is_displayed()
    highlight(faq_label)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

    read_news_button = page_open.read_news_button()
    read_news_button.click()
    time.sleep(1)

    articles_label = home_page.articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    apply_online_button = page_open.apply_online_button()
    apply_online_button.click()
    time.sleep(1)

    convert_your_invoices = page_open.convert_your_invoices_label()
    assert convert_your_invoices.is_displayed()
    highlight(convert_your_invoices)

    driver.back()
    time.sleep(2)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    products_label = home_page.your_working_label()
    assert products_label.text == "Your working capital platform"
    highlight(products_label)

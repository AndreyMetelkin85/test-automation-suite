import time
from HeaderButton_Page import HeaderButtons
from BaseApp import highlight
from SocialNetworks_Page import SocialNetworks
from HomePage import HomePage
from Invoicefinancing_Pages import InvoiceFinancing
from ForTrade_Pages import ForTrade
from News_Pages import News
from ContactUs_Pages import ContactUs


def test_buttons_in_header(driver):
    home_page = HomePage(driver)

    page_products_label = home_page.heading_your_working_label()
    assert page_products_label.is_displayed()
    highlight(page_products_label)

    page_header_buttons = HeaderButtons(driver)
    products_button = page_header_buttons.products_button()
    products_button.click()

    page_invoice_financing = InvoiceFinancing(driver)
    convert_label = page_invoice_financing.heading_convert_your_invoices_label()
    assert convert_label.is_displayed()
    highlight(convert_label)

    page_header_button = HeaderButtons(driver)
    solutions_button = page_header_button.solutions_button()
    solutions_button.click()

    page_for_trade = ForTrade(driver)
    boost_your_cash_label = page_for_trade.heading_boost_your_cash_label()
    assert boost_your_cash_label.is_displayed()
    highlight(boost_your_cash_label)

    page_resources_button = HeaderButtons(driver)
    resources_button = page_resources_button.resources_button()
    resources_button.click()

    page_resources_label = News(driver)
    heading_articles_label = page_resources_label.heading_articles_label()
    assert heading_articles_label.is_displayed()
    highlight(heading_articles_label)

    page_contact_us_button = HeaderButtons(driver)
    contact_us_button = page_contact_us_button.contact_us_button()
    contact_us_button.click()

    page_contact_us_label = ContactUs(driver)
    contact_us_label = page_contact_us_label.heading_contact_us_label()
    assert contact_us_label.is_displayed()
    highlight(contact_us_label)


def test_opening_social_networks(driver, slow_scroll):
    home_page = SocialNetworks(driver)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    slow_scroll(driver, scroll_step=100, pause_duration=0.1)

    footer_logo = home_page.footer_logo_sten()
    assert footer_logo.is_displayed()
    highlight(footer_logo)

    linkedin_button = home_page.social_networks()
    linkedin_button[0].click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url_prefix = "https://www.linkedin.com"
    assert current_url.startswith(expected_url_prefix)

    driver.switch_to.window(current_window)

    facebook_button = SocialNetworks(driver)
    facebook_button.social_networks()[2].click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url_prefix = "https://www.facebook.com"
    assert current_url.startswith(expected_url_prefix)

    driver.switch_to.window(current_window)

    twitter_button = SocialNetworks(driver)
    twitter_button.social_networks()[1].click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://twitter.com/i/flow/login?redirect_after_login=%2FStenn_Intl"
    assert current_url == expected_url

    driver.switch_to.window(current_window)

    youtube_button = SocialNetworks(driver)
    youtube_button.social_networks()[3].click()

    driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    expected_url = "https://www.youtube.com/channel/UCVsztAj0QmhKkfu4IKMHUOA"
    assert current_url == expected_url


def test_сlick_and_transitions_home_page(driver, slow_scroll):
    home_page = HomePage(driver)
    home_page_label = home_page.heading_your_working_label()
    assert home_page_label.is_displayed()
    highlight(home_page_label)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    app_for_finance_button = home_page.apply_for_finance_button_1()
    app_for_finance_button.click()
    time.sleep(1)

    right_for_you_label = home_page.right_for_you()
    assert right_for_you_label.is_displayed()
    highlight(right_for_you_label)

    driver.back()
    time.sleep(1)

    list_buttons = home_page.navi_bar_button()
    list_buttons[0].click()
    time.sleep(1)

    invoice_financing_label = home_page.invoice_financing_label()
    assert invoice_financing_label.is_displayed()
    highlight(invoice_financing_label)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    apply_finance_button = home_page.apply_for_finance_button_2()
    apply_finance_button.click()
    time.sleep(1)

    convert_your_invoices_label = home_page.convert_your_invoices_label()
    assert convert_your_invoices_label.is_displayed()
    highlight(convert_your_invoices_label)

    driver.back()
    time.sleep(2)

    list_buttons = home_page.navi_bar_button()
    list_buttons[1].click()
    time.sleep(1)

    e_commerce_label = home_page.e_commerce_label()
    assert e_commerce_label.is_displayed()
    highlight(e_commerce_label)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    e_commerce_button = home_page.apply_for_finance_button_2()
    e_commerce_button.click()
    time.sleep(1)

    current_url = driver.current_url
    expected_url = "https://rbf.stenn.com/auth/sign-up"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    list_buttons = home_page.navi_bar_button()
    list_buttons[2].click()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    saas_label = home_page.saas_label()
    assert saas_label.is_displayed()
    highlight(saas_label)

    apply_finance_saas_button = home_page.apply_for_finance_button_2()
    apply_finance_saas_button.click()
    time.sleep(1)

    financing_solution_label = home_page.looking_financing_label()
    assert financing_solution_label.is_displayed()

    driver.back()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 1200);")
    time.sleep(2)

    articles_label = home_page.what_stenn_label()
    assert articles_label[0].is_displayed()
    highlight(articles_label[0])

    articles_read_more_button = home_page.what_stenn_button()
    articles_read_more_button[0].click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.heading_articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)

    driver.back()
    time.sleep(2)

    useful_guides_label = home_page.what_stenn_label()
    assert useful_guides_label[1].is_displayed()
    highlight(useful_guides_label[1])

    driver.execute_script("window.scrollBy(0, 1800);")
    time.sleep(2)
    useful_guides_button = home_page.what_stenn_button()
    useful_guides_button[1].click()
    time.sleep(1)

    useful_guides_label = home_page.useful_guides_label()
    assert useful_guides_label.is_displayed()
    highlight(useful_guides_label)

    driver.back()
    time.sleep(2)

    careers_label = home_page.what_stenn_label()
    assert careers_label[2].is_displayed()
    highlight(careers_label[2])

    careers_button = home_page.what_stenn_button()
    careers_button[2].click()
    time.sleep(1)

    careers_label = home_page.join_stenn_label()
    assert careers_label.is_displayed()
    highlight(careers_label)

    driver.back()
    time.sleep(2)

    faq_label = home_page.what_stenn_label()
    assert faq_label[3].is_displayed()
    highlight(faq_label[3])

    faq_button = home_page.what_stenn_button()
    faq_button[3].click()
    time.sleep(1)

    faq_label = home_page.questions_answers_label()
    assert faq_label.is_displayed()
    highlight(faq_label)

    driver.back()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

    read_news_button = home_page.read_news_button()
    read_news_button.click()
    time.sleep(1)

    articles_label = page_articles_label.heading_articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)

    driver.back()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    apply_online_button = home_page.apply_online_button()
    apply_online_button.click()
    time.sleep(1)

    convert_your_invoices_label = home_page.convert_your_invoices_label()
    assert convert_your_invoices_label.is_displayed()
    highlight(convert_your_invoices_label)

    driver.back()
    time.sleep(2)

    products_label = home_page.heading_your_working_label()
    assert products_label.is_displayed()
    highlight(products_label)

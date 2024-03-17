import time
from framework.pages.website_stenn.header_button_page import header_buttons_fixture
from base_page import highlight
from framework.pages.website_stenn.revenue_based_financing_page import revenue_based_financing_page_fixture
from framework.pages.website_stenn.home_page import HomePage
from framework.pages.website_stenn.invoice_financing_page import invoice_financing_page_fixture
from framework.pages.website_stenn.news_page import News
from conftest import driver


def test_invoice_financing_page(driver):
    home_page = header_buttons_fixture(driver)

    products_button = home_page.products_button()
    products_button.click()
    highlight(products_button)

    invoice_financing_page = invoice_financing_page_fixture(driver)
    convert_your_invoices_label = invoice_financing_page.heading_convert_your_invoices_label()
    convert_your_invoices_label.is_displayed()
    highlight(convert_your_invoices_label)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    apply_finance_button_count = 4
    for finance_option_button in range(apply_finance_button_count):
        apply_finance_button = invoice_financing_page.apply_for_finance_button()
        apply_finance_button[finance_option_button].click()

        sign_up_page = invoice_financing_page_fixture(driver)
        convert_your_invoices = sign_up_page.get_heading_label()
        assert convert_your_invoices.is_displayed()
        highlight(convert_your_invoices)

        driver.back()
        time.sleep(1)

        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(0.5)

    learn_more_button = invoice_financing_page.learn_more_button()
    learn_more_button.click()
    time.sleep(1)

    learn_more_label = invoice_financing_page.stenn_named_label()
    assert learn_more_label.is_displayed()
    highlight(learn_more_label)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    asked_questions_button_count = 4
    for number_buttons in range(asked_questions_button_count):
        asked_questions_button = invoice_financing_page.asked_questions_button()
        asked_questions_button[number_buttons].click()
        time.sleep(1)

        if number_buttons == 0:
            how_it_works_label = invoice_financing_page.how_it_works_label()
            assert how_it_works_label.is_displayed()
            highlight(how_it_works_label)
            asked_questions_button[number_buttons].click()
        elif number_buttons == 1:
            almost_any_company_label = invoice_financing_page.almost_any_company_label()
            assert almost_any_company_label.is_displayed()
            highlight(almost_any_company_label)
            asked_questions_button[number_buttons].click()
        elif number_buttons == 2:
            six_benefits_label = invoice_financing_page.six_benefits_label()
            assert six_benefits_label.is_displayed()
            highlight(six_benefits_label)
            asked_questions_button[number_buttons].click()
        elif number_buttons == 3:
            we_finance_label = invoice_financing_page.we_finance_label()
            assert we_finance_label[0].is_displayed()
            highlight(we_finance_label[0])

        driver.execute_script(f"window.scrollBy(0, {50 * (number_buttons + 1)});")
        time.sleep(1)

    apply_finance = HomePage(driver)
    apply_finance_button = apply_finance.apply_for_finance_button()
    apply_finance_button[0].click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    sign_up_page = invoice_financing_page_fixture(driver)
    convert_your_invoices = sign_up_page.get_heading_label()
    assert convert_your_invoices.is_displayed()
    highlight(convert_your_invoices)

    driver.switch_to.window(current_window)

    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)

    invoice_financing_page = HomePage(driver)
    read_news_button = invoice_financing_page.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.get_heading_label()
    assert articles_label.is_displayed()
    highlight(articles_label)


def test_revenue_based_financing(driver):
    home_page = header_buttons_fixture(driver)

    products_button = home_page.products_button()
    products_button.click()
    time.sleep(0.5)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    revenue_based_financing = revenue_based_financing_page_fixture(driver)
    revenue_based_financing_button = revenue_based_financing.revenue_based_financing_button()
    revenue_based_financing_button.click()

    are_you_e_commerce_label = revenue_based_financing.get_heading_label()
    assert are_you_e_commerce_label.is_displayed()

    check_my_limit_button = revenue_based_financing.check_my_limit_button()
    check_my_limit_button.click()

    current_url = driver.current_url
    expected_url_prefix = "https://rbf.stenn.com"
    assert current_url.startswith(expected_url_prefix)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 650);")
    time.sleep(1)

    flexible_financing_options_label = revenue_based_financing.flexible_financing_options_label()
    assert flexible_financing_options_label
    apply_for_finance = revenue_based_financing.apply_for_finance_button()
    apply_for_finance[0].click()

    current_url = driver.current_url
    expected_url_prefix = "https://rbf.stenn.com"
    assert current_url.startswith(expected_url_prefix)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 1200);")
    time.sleep(1)

    unlock_e_commerce_label = revenue_based_financing.unlock_e_commerce_label()
    assert unlock_e_commerce_label.is_displayed()
    apply_for_finance = revenue_based_financing.apply_for_finance_button()
    apply_for_finance[1].click()

    current_url = driver.current_url
    expected_url_prefix = "https://rbf.stenn.com"
    assert current_url.startswith(expected_url_prefix)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 1800);")
    time.sleep(1.5)

    drive_saas_growth_label = revenue_based_financing.drive_saas_growth_label()
    assert drive_saas_growth_label.is_displayed()
    apply_for_finance = revenue_based_financing.apply_for_finance_button()
    apply_for_finance[2].click()

    current_url = driver.current_url
    expected_url_prefix = "https://rbf.stenn.com"
    assert current_url.startswith(expected_url_prefix)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 3000);")
    time.sleep(1)

    learn_more_button = revenue_based_financing.learn_more_button()
    learn_more_button.click()

    learn_more_label = revenue_based_financing.stenn_named_label()
    assert learn_more_label.is_displayed()

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 650);")
    time.sleep(2)

    frequently_asked_questions_count = 5
    for number_buttons in range(frequently_asked_questions_count):
        frequently_asked_questions_button = revenue_based_financing.frequently_asked_questions()
        frequently_asked_questions_button[number_buttons].click()
        time.sleep(1)

        if number_buttons == 0:
            revenue_based_financing_label = revenue_based_financing.revenue_based_financing_label()
            assert revenue_based_financing_label.is_displayed()
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 1:
            typically_our_customers_label = revenue_based_financing.typically_our_customers_label()
            assert typically_our_customers_label.is_displayed()
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 2:
            repayments_for_your_draw_label = revenue_based_financing.repayments_for_your_draw_label()
            assert repayments_for_your_draw_label.is_displayed()
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 3:
            in_order_to_accurately_label = revenue_based_financing.in_order_to_accurately_label()
            assert in_order_to_accurately_label.is_displayed()
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 4:
            sten_is_uk_label = revenue_based_financing.sten_is_uk_label()
            assert sten_is_uk_label.is_displayed()
            frequently_asked_questions_button[number_buttons].click()

    driver.execute_script("window.scrollBy(0, 750);")
    time.sleep(2)

    invoice_financing_page = HomePage(driver)
    read_news_button = invoice_financing_page.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.get_heading_label()
    assert articles_label.is_displayed()

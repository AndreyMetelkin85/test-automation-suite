import time
from conftest import driver
from selenium.webdriver.common.action_chains import ActionChains
from framework.page_fixture import header_buttons_fixture, revenue_based_financing_page_fixture, \
    home_page_fixture, invoice_financing_page_fixture, news_page_fixture, articles_page_fixture


def test_apply_for_finance_button_in_invoice_financing_page(
        driver, header_buttons_fixture, invoice_financing_page_fixture, home_page_fixture):
    accept_all_cookies_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    products_button = header_buttons_fixture.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    invoice_financing_button = header_buttons_fixture.financing_hover_button()
    actions.move_to_element(invoice_financing_button[0])
    actions.click(invoice_financing_button[0]).perform()

    apply_finance_button_count = 4
    for finance_option_button in range(apply_finance_button_count):
        apply_finance_button = invoice_financing_page_fixture.apply_for_finance_button()
        driver.execute_script("arguments[0].click();", apply_finance_button[finance_option_button])
        time.sleep(1.5)

        driver.switch_to.window(driver.window_handles[1])

        current_url = driver.current_url
        expected_url = "https://app.stenn.com/auth/sign-up"
        assert current_url == expected_url

        driver.switch_to.window(driver.window_handles[0])

        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(0.5)


def test_information_unveiling(driver, invoice_financing_page_fixture, home_page_fixture, news_page_fixture,
                               articles_page_fixture):
    driver.get('https://www.stenn.com/product/invoice-financing')

    accept_all_cookies_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    driver.execute_script("window.scrollBy(0, 3700);")
    time.sleep(1)

    asked_questions_button_count = 4
    for number_count_buttons in range(asked_questions_button_count):
        asked_questions_button = invoice_financing_page_fixture.asked_questions_button()
        asked_questions_button[number_count_buttons].click()
        time.sleep(1)

        if number_count_buttons == 0:
            how_it_works_label = invoice_financing_page_fixture.how_it_works_label()
            assert how_it_works_label.is_displayed()
            how_it_works_button = invoice_financing_page_fixture.how_it_works_button()
            how_it_works_button.click()
        elif number_count_buttons == 1:
            almost_any_company_label = invoice_financing_page_fixture.almost_any_company_label()
            assert almost_any_company_label.is_displayed()
            almost_any_company_button = invoice_financing_page_fixture.almost_any_company_button()
            almost_any_company_button.click()
        elif number_count_buttons == 2:
            six_benefits_label = invoice_financing_page_fixture.six_benefits_label()
            assert six_benefits_label.is_displayed()
            six_benefits_of_stsnn_financing_button = invoice_financing_page_fixture.six_benefits_of_stenn_financing_button()
            six_benefits_of_stsnn_financing_button.click()
        elif number_count_buttons == 3:
            we_finance_label = invoice_financing_page_fixture.stenn_pricing_information()
            assert we_finance_label[0].is_displayed()
            fees_starting_button = invoice_financing_page_fixture.fees_starting_button()
            fees_starting_button.click()

        driver.execute_script(f"window.scrollBy(0, {50 * (number_count_buttons + 1)});")
        time.sleep(1)

    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(1)

    read_all_news_button = home_page_fixture.read_news_button()
    read_all_news_button.click()
    articles_label = articles_page_fixture.get_heading_label()
    assert articles_label.is_displayed()


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

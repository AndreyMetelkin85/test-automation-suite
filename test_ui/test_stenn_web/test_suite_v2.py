import time
from test_ui.conftest import driver, wait, page_fixture
from selenium.webdriver.common.action_chains import ActionChains


def test_apply_for_finance_button_in_invoice_financing_page(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    products_button = page_fixture.header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    invoice_financing_button = page_fixture.header_buttons.financing_hover_button()
    actions.move_to_element(invoice_financing_button[0])
    actions.click(invoice_financing_button[0]).perform()

    apply_finance_button_count = 4
    for finance_option_button in range(apply_finance_button_count):
        apply_finance_button = page_fixture.invoice_financing_page.apply_for_finance_button()
        driver.execute_script("arguments[0].click();", apply_finance_button[finance_option_button])

        driver.switch_to.window(driver.window_handles[1])

        expected_url = "https://app.stenn.com/auth/sign-up"
        wait.wait_until_the_url_is_visible(expected_url)
        current_url = driver.current_url
        assert current_url == expected_url

        driver.switch_to.window(driver.window_handles[0])

        driver.execute_script("window.scrollBy(0, 700);")


def test_information_unveiling_frequently_asked_questions_block_invoice_financing_page(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    driver.get('https://www.stenn.com/product/invoice-financing')

    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    driver.execute_script("window.scrollBy(0, 3600);")
    time.sleep(1)

    asked_questions_button_count = 4
    for number_count_buttons in range(asked_questions_button_count):
        asked_questions_button = page_fixture.invoice_financing_page.asked_questions_button()
        asked_questions_button[number_count_buttons].click()

        if number_count_buttons == 0:
            how_it_works_label = page_fixture.invoice_financing_page.how_it_works_label()
            assert how_it_works_label.is_displayed()
            how_it_works_button = page_fixture.invoice_financing_page.how_it_works_button()
            how_it_works_button.click()

        elif number_count_buttons == 1:
            almost_any_company_label = page_fixture.invoice_financing_page.almost_any_company_label()
            assert almost_any_company_label.is_displayed()
            almost_any_company_button = page_fixture.invoice_financing_page.almost_any_company_button()
            almost_any_company_button.click()

        elif number_count_buttons == 2:
            six_benefits_label = page_fixture.invoice_financing_page.six_benefits_label()
            assert six_benefits_label.is_displayed()
            six_benefits_of_stenn_financing_button = \
                page_fixture.invoice_financing_page.six_benefits_of_stenn_financing_button()
            six_benefits_of_stenn_financing_button.click()

        elif number_count_buttons == 3:
            we_finance_label = page_fixture.invoice_financing_page.stenn_pricing_information()
            wait.wait_until_the_element_is_visible(we_finance_label)
            assert we_finance_label.is_displayed()
            fees_starting_button = page_fixture.invoice_financing_page.fees_starting_button()
            fees_starting_button.click()

        driver.execute_script(f"window.scrollBy(0, {55 * (number_count_buttons + 1)});")
        time.sleep(1)

    driver.execute_script("window.scrollBy(0, 600);")

    read_all_news_button = page_fixture.home_page.read_news_button()
    read_all_news_button.click()
    articles_label = page_fixture.articles_page.get_heading_label()
    wait.wait_until_the_element_is_visible(articles_label)
    assert articles_label.is_displayed()


def test_apply_for_finance_button_in_revenue_based_financing_page(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    driver.get('https://www.stenn.com/product/revenue-based-financing')

    accept_all_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_button.click()

    check_my_limit_button = page_fixture.revenue_based_financing_page.check_my_limit_button()
    check_my_limit_button.click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://rbf.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    driver.execute_script("window.scrollBy(0, 1000);")

    flexible_financing_options_label = page_fixture.revenue_based_financing_page.flexible_financing_options_label()
    wait.wait_until_the_element_is_visible(flexible_financing_options_label)
    assert flexible_financing_options_label.is_displayed()
    apply_for_finance = page_fixture.revenue_based_financing_page.apply_for_finance_button()
    apply_for_finance[0].click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://rbf.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    driver.execute_script("window.scrollBy(0, 1200);")

    unlock_e_commerce_label = page_fixture.revenue_based_financing_page.unlock_e_commerce_label()
    wait.wait_until_the_element_is_visible(unlock_e_commerce_label)
    assert unlock_e_commerce_label.is_displayed()
    apply_for_finance = page_fixture.revenue_based_financing_page.apply_for_finance_button()
    apply_for_finance[3].click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://rbf.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url


def test_information_unveiling_frequently_asked_questions_block_revenue_based_financing_page(driver, page_fixture,
                                                                                             wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    driver.get('https://www.stenn.com/product/revenue-based-financing')

    accept_all_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_button.click()

    driver.execute_script("window.scrollBy(0, 4700);")

    frequently_asked_questions_count = 5
    for number_buttons in range(frequently_asked_questions_count):
        frequently_asked_questions_button = page_fixture.revenue_based_financing_page.frequently_asked_questions()
        frequently_asked_questions_button[number_buttons].click()

        if number_buttons == 0:
            revenue_based_financing_label = page_fixture.revenue_based_financing_page.revenue_based_financing_label()
            wait.wait_until_the_element_is_visible(revenue_based_financing_label)
            assert revenue_based_financing_label.is_displayed()
            what_is_revenue_button = page_fixture.revenue_based_financing_page.what_is_revenue_button()
            what_is_revenue_button.click()
        elif number_buttons == 1:
            typically_our_customers_label = page_fixture.revenue_based_financing_page.typically_our_customers_label()
            wait.wait_until_the_element_is_visible(typically_our_customers_label)
            assert typically_our_customers_label.is_displayed()
            what_can_i_use_button = page_fixture.revenue_based_financing_page.what_can_i_use_button()
            what_can_i_use_button.click()
        elif number_buttons == 2:
            repayments_for_your_draw_label = page_fixture.revenue_based_financing_page.repayments_for_your_draw_label()
            wait.wait_until_the_element_is_visible(repayments_for_your_draw_label)
            assert repayments_for_your_draw_label.is_displayed()
            how_do_repayments_work_button = page_fixture.revenue_based_financing_page.how_do_repayments_work_button()
            how_do_repayments_work_button.click()
        elif number_buttons == 3:
            in_order_to_accurately_label = page_fixture.revenue_based_financing_page.in_order_to_accurately_label()
            wait.wait_until_the_element_is_visible(in_order_to_accurately_label)
            assert in_order_to_accurately_label.is_displayed()
            what_information_do_button = page_fixture.revenue_based_financing_page.what_information_do_button()
            what_information_do_button.click()
        elif number_buttons == 4:
            sten_is_uk_label = page_fixture.revenue_based_financing_page.sten_is_uk_label()
            wait.wait_until_the_element_is_visible(sten_is_uk_label)
            assert sten_is_uk_label.is_displayed()
            who_is_stenn = page_fixture.revenue_based_financing_page.who_is_stenn()
            who_is_stenn.click()

    driver.execute_script("window.scrollBy(0, 650);")

    read_news_button = page_fixture.revenue_based_financing_page.read_news_button()
    read_news_button.click()

    articles_label = page_fixture.articles_page.get_heading_label()
    wait.wait_until_the_element_is_visible(articles_label)
    assert articles_label.is_displayed()

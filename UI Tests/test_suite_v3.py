import time
from selenium.webdriver.common.action_chains import ActionChains
from conftest import driver, page_fixture, wait


def test_for_trade_page(driver, page_fixture, wait):
    driver.get('https://www.stenn.com/solutions/trade')

    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    apply_finance_button = page_fixture.for_trade_page.apply_for_finance_button()
    apply_finance_button.click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://app.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1)

    button_counter = 3
    for button in range(button_counter):
        asked_questions = page_fixture.for_trade_page.frequently_asked_questions_button()
        asked_questions[button].click()
        time.sleep(1)

        if button == 0:
            how_it_works_label = page_fixture.for_trade_page.how_it_works_label()
            assert how_it_works_label.is_displayed()
            how_it_works_button = page_fixture.for_trade_page.how_it_works_button()
            how_it_works_button.click()
        elif button == 1:
            almost_any_company_label = page_fixture.for_trade_page.almost_any_company_label()
            assert almost_any_company_label.is_displayed()
            almost_any_company_button = page_fixture.for_trade_page.almost_any_company_button()
            almost_any_company_button.click()
        elif button == 2:
            six_benefits_label = page_fixture.for_trade_page.six_benefits_label()
            assert six_benefits_label.is_displayed()
            six_benefits_of_stenn_financing_button = \
                page_fixture.for_trade_page.six_benefits_of_stenn_financing_button()
            six_benefits_of_stenn_financing_button.click()

        driver.execute_script("window.scrollBy(0, 90);")
        time.sleep(1)

    driver.execute_script("window.scrollBy(0, 1900);")
    time.sleep(2)

    news_button = page_fixture.for_trade_page.read_news_button()
    news_button.click()
    articles_label = page_fixture.articles_page.get_heading_label()
    wait.wait_until_the_element_is_visible(articles_label)
    assert articles_label.is_displayed()


def test_e_commerce(driver, wait, page_fixture):
    driver.get('https://www.stenn.com/solutions/ecommerce-financing')

    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    check_my_limit_button = page_fixture.for_e_commerce_page.check_my_limit_button()
    check_my_limit_button.click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://rbf.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    driver.execute_script("window.scrollBy(0, 2700);")

    button_counter = 5
    for buttons in range(button_counter):
        frequent_lyasked_questions_button = page_fixture.for_e_commerce_page.frequently_asked_questions()
        frequent_lyasked_questions_button[buttons].click()

        if buttons == 0:
            revenue_based_financing_label = page_fixture.for_e_commerce_page.revenue_based_financing_label()
            wait.wait_until_the_element_is_visible(revenue_based_financing_label)
            assert revenue_based_financing_label.is_displayed()
            what_is_revenue_button = page_fixture.for_e_commerce_page.what_is_revenue_button()
            what_is_revenue_button.click()
        elif buttons == 1:
            typically_our_customers_label = page_fixture.for_e_commerce_page.typically_our_customers_label()
            wait.wait_until_the_element_is_visible(typically_our_customers_label)
            assert typically_our_customers_label.is_displayed()
            what_can_i_use_button = page_fixture.for_e_commerce_page.what_can_i_use_button()
            what_can_i_use_button.click()
        elif buttons == 2:
            repayments_for_your_draw_label = page_fixture.for_e_commerce_page.repayments_for_your_draw_label()
            wait.wait_until_the_element_is_visible(repayments_for_your_draw_label)
            assert repayments_for_your_draw_label.is_displayed()
            how_do_repayments_work_button = page_fixture.for_e_commerce_page.how_do_repayments_work_button()
            how_do_repayments_work_button.click()
        elif buttons == 3:
            in_order_to_accurately_label = page_fixture.for_e_commerce_page.in_order_to_accurately_label()
            wait.wait_until_the_element_is_visible(in_order_to_accurately_label)
            assert in_order_to_accurately_label.is_displayed()
            what_information_do_button = page_fixture.for_e_commerce_page.what_information_do_button()
            what_information_do_button.click()
        elif buttons == 4:
            sten_is_uk_label = page_fixture.for_e_commerce_page.sten_is_uk_label()
            wait.wait_until_the_element_is_visible(sten_is_uk_label)
            assert sten_is_uk_label.is_displayed()
            who_is_stenn = page_fixture.for_e_commerce_page.who_is_stenn()
            who_is_stenn.click()

    driver.execute_script("window.scrollBy(0, 1000);")

    news_button = page_fixture.for_e_commerce_page.read_news_button()
    news_button.click()
    time.sleep(1)

    articles_label = page_fixture.articles_page.get_heading_label()
    assert articles_label.is_displayed()


def test_saas_page(driver, wait, page_fixture):
    driver.get('https://www.stenn.com/solutions/saas')

    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    privacy_policy_button = page_fixture.saas_page.privacy_policy_button()
    privacy_policy_button.click()

    driver.switch_to.window(driver.window_handles[1])

    expected_prefix = 'https://app.stenn.com/privacy-policy'
    wait.wait_until_url_contains(expected_prefix)
    current_url = driver.current_url
    assert current_url.startswith(expected_prefix), f"URL {current_url} does not start with {expected_prefix}"

    privacy_policy_label = page_fixture.saas_page.privacy_policy_label()
    privacy_policy_label.is_displayed()

    driver.switch_to.window(driver.window_handles[0])

    driver.execute_script("window.scrollBy(0, 1000);")

    join_beta_button = page_fixture.saas_page.join_the_beta_button()
    join_beta_button.click()
    time.sleep(1.5)

    driver.execute_script("window.scrollBy(0, 2650);")

    button_counter = 5
    for buttons in range(button_counter):
        frequent_lyasked_questions_button = page_fixture.saas_page.frequently_asked_questions()
        frequent_lyasked_questions_button[buttons].click()
        time.sleep(1)

        if buttons == 0:
            revenue_based_financing_label = page_fixture.saas_page.revenue_based_financing_label()
            wait.wait_until_the_element_is_visible(revenue_based_financing_label)
            assert revenue_based_financing_label.is_displayed()
            what_is_revenue_button = page_fixture.saas_page.what_is_revenue_button()
            what_is_revenue_button.click()
        elif buttons == 1:
            typically_our_customers_label = page_fixture.saas_page.typically_our_customers_label()
            wait.wait_until_the_element_is_visible(typically_our_customers_label)
            assert typically_our_customers_label.is_displayed()
            what_can_i_use_button = page_fixture.saas_page.what_can_i_use_button()
            what_can_i_use_button.click()
        elif buttons == 2:
            repayments_for_your_draw_label = page_fixture.saas_page.repayments_for_your_draw_label()
            wait.wait_until_the_element_is_visible(repayments_for_your_draw_label)
            assert repayments_for_your_draw_label.is_displayed()
            how_do_repayments_work_button = page_fixture.saas_page.how_do_repayments_work_button()
            how_do_repayments_work_button.click()
        elif buttons == 3:
            in_order_to_accurately_label = page_fixture.saas_page.in_order_to_accurately_label()
            wait.wait_until_the_element_is_visible(in_order_to_accurately_label)
            assert in_order_to_accurately_label.is_displayed()
            what_information_do_button = page_fixture.saas_page.what_information_do_button()
            what_information_do_button.click()
        elif buttons == 4:
            sten_is_uk_label = page_fixture.saas_page.sten_is_uk_label()
            wait.wait_until_the_element_is_visible(sten_is_uk_label)
            assert sten_is_uk_label.is_displayed()
            who_is_stenn = page_fixture.saas_page.who_is_stenn()
            who_is_stenn.click()

    driver.execute_script("window.scrollBy(0, 1000);")

    news_button = page_fixture.for_e_commerce_page.read_news_button()
    news_button.click()
    time.sleep(1)

    articles_label = page_fixture.articles_page.get_heading_label()
    assert articles_label.is_displayed()

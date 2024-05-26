from plugins.tools_plugin import driver, page_fixture, wait, scroll_down


def test_trade_page_functionality(driver, page_fixture, wait, scroll_down):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
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

    scroll_down(800)

    labels_and_buttons = [
        ("how_it_works",
         page_fixture.for_trade_page.how_it_works_label, page_fixture.for_trade_page.how_it_works_button),
        ("almost_any_company",
         page_fixture.for_trade_page.almost_any_company_label, page_fixture.for_trade_page.almost_any_company_button),
        ("six_benefits",
         page_fixture.for_trade_page.six_benefits_label,
         page_fixture.for_trade_page.six_benefits_of_stenn_financing_button)
    ]

    for button_id, label_element_func, button_element_func in labels_and_buttons:
        current_button_element = button_element_func()
        current_button_element.click()
        label_element = label_element_func()
        wait.wait_until_the_element_is_visible(label_element)
        assert label_element.is_displayed()
        current_button_element.click()
        scroll_down(90)

    scroll_down(1900)

    news_button = page_fixture.for_trade_page.read_news_button()
    news_button.click()
    articles_label = page_fixture.articles_page.get_heading_label()
    wait.wait_until_the_element_is_visible(articles_label)
    assert articles_label.is_displayed()


def test_e_commerce_page_functionality(driver, wait, page_fixture, scroll_down):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
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

    scroll_down(2700)

    labels_and_buttons = [
        ("revenue_based_financing", page_fixture.for_e_commerce_page.revenue_based_financing_label,
         page_fixture.for_e_commerce_page.what_is_revenue_button),
        ("typically_our_customers", page_fixture.for_e_commerce_page.typically_our_customers_label,
         page_fixture.for_e_commerce_page.what_can_i_use_button),
        ("repayments_for_your_draw", page_fixture.for_e_commerce_page.repayments_for_your_draw_label,
         page_fixture.for_e_commerce_page.how_do_repayments_work_button),
        ("in_order_to_accurately", page_fixture.for_e_commerce_page.in_order_to_accurately_label,
         page_fixture.for_e_commerce_page.what_information_do_button),
        ("sten_is_uk", page_fixture.for_e_commerce_page.sten_is_uk_label, page_fixture.for_e_commerce_page.who_is_stenn)
    ]

    for button_id, label_element_func, button_element_func in labels_and_buttons:
        current_button_element = button_element_func()
        current_button_element.click()
        label_element = label_element_func()
        wait.wait_until_the_element_is_visible(label_element)
        assert label_element.is_displayed()
        current_button_element.click()

    scroll_down(1000)

    news_button = page_fixture.for_e_commerce_page.read_news_button()
    news_button.click()
    articles_label = page_fixture.articles_page.get_heading_label()
    assert articles_label.is_displayed()


def test_saas_page_functionality(driver, wait, page_fixture, scroll_down):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    driver.get('https://www.stenn.com/solutions/saas')

    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    privacy_policy_button = page_fixture.saas_page.privacy_policy_button()
    privacy_policy_button.click()

    driver.switch_to.window(driver.window_handles[1])

    expected_prefix = 'https://www.stenn.com/privacy-policy'
    wait.wait_until_url_contains(expected_prefix)
    current_url = driver.current_url
    assert current_url.startswith(expected_prefix), f"URL {current_url} does not start with {expected_prefix}"

    driver.switch_to.window(driver.window_handles[0])

    scroll_down(1000)

    join_beta_button = page_fixture.saas_page.join_the_beta_button()
    join_beta_button.click()

    scroll_down(2800)

    labels_and_buttons = [
        ("revenue_based_financing", page_fixture.for_e_commerce_page.revenue_based_financing_label,
         page_fixture.for_e_commerce_page.what_is_revenue_button),
        ("typically_our_customers", page_fixture.for_e_commerce_page.typically_our_customers_label,
         page_fixture.for_e_commerce_page.what_can_i_use_button),
        ("repayments_for_your_draw", page_fixture.for_e_commerce_page.repayments_for_your_draw_label,
         page_fixture.for_e_commerce_page.how_do_repayments_work_button),
        ("in_order_to_accurately", page_fixture.for_e_commerce_page.in_order_to_accurately_label,
         page_fixture.for_e_commerce_page.what_information_do_button),
        ("sten_is_uk", page_fixture.for_e_commerce_page.sten_is_uk_label, page_fixture.for_e_commerce_page.who_is_stenn)
    ]

    for button_id, label_element_func, button_element_func in labels_and_buttons:
        current_button_element = button_element_func()
        current_button_element.click()
        label_element = label_element_func()
        wait.wait_until_the_element_is_visible(label_element)
        assert label_element.is_displayed()
        current_button_element.click()

    scroll_down(1000)

    news_button = page_fixture.for_e_commerce_page.read_news_button()
    news_button.click()
    articles_label = page_fixture.articles_page.get_heading_label()
    assert articles_label.is_displayed()

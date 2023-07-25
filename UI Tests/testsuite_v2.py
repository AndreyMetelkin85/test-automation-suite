import time
from HeaderButton_Page import HeaderButtons
from BaseApp import highlight
from RevenueBasedFinancing_Page import RevenueBasedFinancing
from HomePage import HomePage
from Invoicefinancing_Pages import InvoiceFinancing
from News_Pages import News


def test_invoice_financing_page(driver):
    home_page = HeaderButtons(driver)

    products_button = home_page.products_button()
    products_button.click()
    highlight(products_button)

    invoice_financing_page = InvoiceFinancing(driver)
    convert_your_invoices_label = invoice_financing_page.heading_convert_your_invoices_label()
    convert_your_invoices_label.is_displayed()
    highlight(convert_your_invoices_label)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    apply_finance_button_count = 4
    for finance_option_button in range(apply_finance_button_count):
        apply_finance_button = invoice_financing_page.apply_for_finance_button()
        apply_finance_button[finance_option_button].click()

        sign_up_page = InvoiceFinancing(driver)
        convert_your_invoices = sign_up_page.sign_up_heading_convert_your_label()
        assert convert_your_invoices.is_displayed()
        highlight(convert_your_invoices)

        driver.back()
        time.sleep(1)

        driver.execute_script(f"window.scrollBy(0, {700 * (finance_option_button + 1)});")
        time.sleep(1)

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
    sign_up_page = InvoiceFinancing(driver)
    convert_your_invoices = sign_up_page.sign_up_heading_convert_your_label()
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
    articles_label = page_articles_label.heading_articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)


def test_revenue_based_financing(driver):
    home_page = HeaderButtons(driver)

    products_button = home_page.products_button()
    products_button.click()
    time.sleep(1)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    revenue_based_financing = RevenueBasedFinancing(driver)
    revenue_based_financing_button = revenue_based_financing.revenue_based_financing_button()
    revenue_based_financing_button.click()

    are_you_e_commerce_label = revenue_based_financing.are_you_e_commerce_label()
    assert are_you_e_commerce_label.is_displayed()
    highlight(are_you_e_commerce_label)

    check_my_limit_button = revenue_based_financing.check_my_limit_button()
    check_my_limit_button.click()

    current_url = driver.current_url
    expected_url_prefix = "https://rbf.stenn.com"
    assert current_url.startswith(expected_url_prefix)

    driver.back()
    time.sleep(1)

    flexible_financing_options_label = revenue_based_financing.flexible_financing_options_label()
    driver.execute_script("arguments[0].scrollIntoView();", flexible_financing_options_label)
    time.sleep(2)
    assert flexible_financing_options_label.is_displayed()
    highlight(flexible_financing_options_label)

    count_buttons = 3
    scroll_distance = 1300
    for finance_button in range(count_buttons):
        if finance_button == 1:
            unlock_e_commerce_label = revenue_based_financing.unlock_e_commerce_label()
            assert unlock_e_commerce_label.is_displayed()
            highlight(unlock_e_commerce_label)
        elif finance_button == 2:
            drive_saas_growth = revenue_based_financing.drive_saas_growth_label()
            assert drive_saas_growth.is_displayed()
            highlight(drive_saas_growth)

        apply_for_finance_button = revenue_based_financing.apply_for_finance_button()
        apply_for_finance_button[finance_button].click()
        time.sleep(1)

        current_url = driver.current_url
        expected_url_prefix = "https://rbf.stenn.com"
        assert current_url.startswith(expected_url_prefix)

        driver.back()
        time.sleep(2)

        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(2)
        scroll_distance += 350

    learn_more_button = revenue_based_financing.learn_more_button()
    driver.execute_script("arguments[0].scrollIntoView();", learn_more_button)
    time.sleep(1)
    learn_more_button.click()

    learn_more_label = revenue_based_financing.stenn_named_label()
    assert learn_more_label.is_displayed()
    highlight(learn_more_label)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 75);")
    time.sleep(2)

    frequently_asked_questions_count = 5
    for number_buttons in range(frequently_asked_questions_count):
        frequently_asked_questions_button = revenue_based_financing.frequently_asked_questions()
        frequently_asked_questions_button[number_buttons].click()
        time.sleep(1)

        if number_buttons == 0:
            revenue_based_financing_label = revenue_based_financing.revenue_based_financing_label()
            assert revenue_based_financing_label.is_displayed()
            highlight(revenue_based_financing_label)
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 1:
            typically_our_customers_label = revenue_based_financing.typically_our_customers_label()
            assert typically_our_customers_label.is_displayed()
            highlight(typically_our_customers_label)
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 2:
            repayments_for_your_draw_label = revenue_based_financing.repayments_for_your_draw_label()
            assert repayments_for_your_draw_label.is_displayed()
            highlight(repayments_for_your_draw_label)
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 3:
            in_order_to_accurately_label = revenue_based_financing.in_order_to_accurately_label()
            assert in_order_to_accurately_label.is_displayed()
            highlight(in_order_to_accurately_label)
            frequently_asked_questions_button[number_buttons].click()
        elif number_buttons == 4:
            sten_is_uk_label = revenue_based_financing.sten_is_uk_label()
            assert sten_is_uk_label.is_displayed()
            highlight(sten_is_uk_label)
            frequently_asked_questions_button[number_buttons].click()

    driver.execute_script("window.scrollBy(0, 750);")
    time.sleep(2)

    invoice_financing_page = HomePage(driver)
    read_news_button = invoice_financing_page.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.heading_articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)
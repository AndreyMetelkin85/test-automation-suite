import time
from framework.pages.website_stenn.for_e_commerce_page import ForECommerce
from framework.pages.website_stenn.for_trade_page import ForTrade
from framework.pages.website_stenn.header_button_page import HeaderButtons
from framework.pages.website_stenn.home_page import HomePage
from framework.pages.website_stenn.news_page import News
from framework.pages.website_stenn.saas_page import Saas
from conftest import driver


def test_for_trade_page(driver):
    home_page = HeaderButtons(driver)

    solutions_button = home_page.solutions_button()
    solutions_button.click()

    for_trade = ForTrade(driver)

    for_trade_page = for_trade.get_heading_label()
    assert for_trade_page.is_displayed()

    close_popup = for_trade.accept_all_pop_up_button()
    close_popup.click()

    apply_finance = for_trade.apply_for_finance_button()
    apply_finance.click()

    sign_up_page = for_trade.convert_your_invoices_label()
    assert sign_up_page.is_displayed()

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1)

    button_counter = 4
    for button in range(button_counter):
        asked_questions = for_trade.frequently_asked_questions_button()
        asked_questions[button].click()
        time.sleep(1)

        if button == 0:
            how_it_works_label = for_trade.how_it_works_label()
            assert how_it_works_label.is_displayed()
            asked_questions[button].click()
        elif button == 1:
            almost_any_company_label = for_trade.almost_any_company_label()
            assert almost_any_company_label.is_displayed()
            asked_questions[button].click()
        elif button == 2:
            six_benefits_label = for_trade.six_benefits_label()
            assert six_benefits_label.is_displayed()
            asked_questions[button].click()
        elif button == 3:
            we_finance_label = for_trade.we_finance_label()
            assert we_finance_label[0].is_displayed()

        driver.execute_script("window.scrollBy(0, 90);")
        time.sleep(1)

    apply_for_finance_button = for_trade.apply_for_finance()
    apply_for_finance_button.click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    sign_up_page = for_trade.convert_your_invoices_label()
    assert sign_up_page.is_displayed()

    driver.switch_to.window(current_window)

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

    learn_more = for_trade.learn_more_button()
    learn_more.click()
    time.sleep(1)

    learn_more_label = for_trade.learn_more_label()
    assert learn_more_label.is_displayed()

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 250);")
    time.sleep(2)

    read_news = HomePage(driver)
    read_news_button = read_news.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.get_heading_label()
    assert articles_label.is_displayed()


def test_e_commerce(driver):
    home_page = HeaderButtons(driver)

    solutions_button = home_page.solutions_button()
    solutions_button.click()
    time.sleep(1)

    close_popup = home_page.accept_all_pop_up_button()
    close_popup.click()

    e_commerce = ForECommerce(driver)
    e_commerce_button = e_commerce.ecommerce_batton()
    e_commerce_button.click()

    e_commerce_page_label = e_commerce.get_heading_label()
    assert e_commerce_page_label.is_displayed()

    check_my_limit_button = e_commerce.check_my_limit_button()
    check_my_limit_button.click()
    time.sleep(1)

    current_url = driver.current_url
    expected_url_prefix = "https://rbf.stenn.com"
    assert current_url.startswith(expected_url_prefix)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 1500);")
    time.sleep(2)

    learn_more = e_commerce.learn_more_button()
    learn_more.click()
    time.sleep(1)

    learn_more_label = e_commerce.learn_more_label()
    assert learn_more_label.is_displayed()

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(2)

    button_counter = 5
    for buttons in range(button_counter):
        frequent_lyasked_questions_button = e_commerce.frequently_asked_questions()
        frequent_lyasked_questions_button[buttons].click()

        if buttons == 0:
            what_revenue_label = e_commerce.revenue_based_financing_label()
            assert what_revenue_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 1:
            what_can_i_use_label = e_commerce.typically_our_customers_label()
            assert what_can_i_use_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 2:
            how_do_repayments_work = e_commerce.repayments_for_your_draw_label()
            assert how_do_repayments_work.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 3:
            what_information_label = e_commerce.in_order_to_accurately_label()
            assert what_information_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 4:
            who_is_stenn_label = e_commerce.sten_is_uk_label()
            assert who_is_stenn_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()

            driver.execute_script("window.scrollBy(0, 100);")
            time.sleep(2)

    driver.execute_script("window.scrollBy(0, 750);")
    time.sleep(2)

    read_news = HomePage(driver)
    read_news_button = read_news.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.get_heading_label()
    assert articles_label.is_displayed()


def test_saas_page(driver):
    home_page = HeaderButtons(driver)

    solutions_button = home_page.solutions_button()
    solutions_button.click()
    time.sleep(1)

    close_popup = home_page.accept_all_pop_up_button()
    close_popup.click()
    time.sleep(1)

    saas_page = Saas(driver)
    saas_button = saas_page.saas_button()
    saas_button[2].click()

    saas_label = saas_page.get_heading_label()
    assert saas_label.is_displayed()

    privacy_policy_button = saas_page.privacy_policy_button()
    privacy_policy_button.click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    privacy_policy_label = saas_page.privacy_policy_label()
    assert privacy_policy_label.is_displayed()

    driver.switch_to.window(current_window)

    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1)

    contact_us_label = saas_page.contact_us_label()
    assert contact_us_label.is_displayed()

    join_the_beta_button = saas_page.join_the_beta_button()
    join_the_beta_button.click()
    time.sleep(1)

    saas_label = saas_page.get_heading_label()
    assert saas_label.is_displayed()

    driver.execute_script("window.scrollBy(0, 2000);")
    time.sleep(2)

    learn_more_button = saas_page.learn_more_button()
    learn_more_button.click()
    time.sleep(1)

    learn_more_label = saas_page.learn_more_label()
    assert learn_more_label.is_displayed()

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 900);")
    time.sleep(2)

    button_counter = 5
    for buttons in range(button_counter):
        frequent_lyasked_questions_button = saas_page.frequently_asked_questions()
        frequent_lyasked_questions_button[buttons].click()
        time.sleep(1)

        if buttons == 0:
            what_revenue_label = saas_page.revenue_based_financing_label()
            assert what_revenue_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 1:
            what_can_i_use_label = saas_page.typically_our_customers_label()
            assert what_can_i_use_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 2:
            how_do_repayments_work = saas_page.repayments_for_your_draw_label()
            assert how_do_repayments_work.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 3:
            what_information_label = saas_page.in_order_to_accurately_label()
            assert what_information_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()
        elif buttons == 4:
            who_is_stenn_label = saas_page.sten_is_uk_label()
            assert who_is_stenn_label.is_displayed()
            frequent_lyasked_questions_button[buttons].click()

            driver.execute_script("window.scrollBy(0, 100);")
            time.sleep(2)

    driver.execute_script("window.scrollBy(0, 750);")
    time.sleep(2)

    read_news = HomePage(driver)
    read_news_button = read_news.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.get_heading_label()
    assert articles_label.is_displayed()

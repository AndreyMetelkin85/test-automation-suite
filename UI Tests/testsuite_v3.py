import time

from base_page import highlight
from for_trade_page import ForTrade
from header_button_page import HeaderButtons
from home_page import HomePage
from news_page import News


def test_for_trade_page(driver):
    home_page = HeaderButtons(driver)

    solutions_button = home_page.solutions_button()
    solutions_button.click()

    for_trade = ForTrade(driver)

    for_trade_page = for_trade.heading_boost_your_cash_label()
    assert for_trade_page.is_displayed()
    highlight(for_trade_page)

    close_popup = for_trade.accept_all_pop_up_button()
    close_popup.click()

    apply_finance = for_trade.apply_for_finance_button()
    apply_finance.click()

    sign_up_page = for_trade.convert_your_invoices_label()
    assert sign_up_page.is_displayed()
    highlight(sign_up_page)

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
            highlight(how_it_works_label)
            asked_questions[button].click()
        elif button == 1:
            almost_any_company_label = for_trade.almost_any_company_label()
            assert almost_any_company_label.is_displayed()
            highlight(almost_any_company_label)
            asked_questions[button].click()
        elif button == 2:
            six_benefits_label = for_trade.six_benefits_label()
            assert six_benefits_label.is_displayed()
            highlight(six_benefits_label)
            asked_questions[button].click()
        elif button == 3:
            we_finance_label = for_trade.we_finance_label()
            assert we_finance_label[0].is_displayed()
            highlight(we_finance_label[0])

        driver.execute_script("window.scrollBy(0, 90);")
        time.sleep(1)

    apply_for_finance_button = for_trade.apply_for_finance()
    apply_for_finance_button.click()

    current_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    sign_up_page = for_trade.convert_your_invoices_label()
    assert sign_up_page.is_displayed()
    highlight(sign_up_page)

    driver.switch_to.window(current_window)

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

    learn_more = for_trade.learn_more_button()
    learn_more.click()
    time.sleep(1)

    learn_more_label = for_trade.learn_more_label()
    assert learn_more_label.is_displayed()
    highlight(learn_more_label)

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 250);")
    time.sleep(2)

    read_news = HomePage(driver)
    read_news_button = read_news.read_news_button()
    read_news_button.click()
    time.sleep(1)

    page_articles_label = News(driver)
    articles_label = page_articles_label.heading_articles_label()
    assert articles_label.is_displayed()
    highlight(articles_label)
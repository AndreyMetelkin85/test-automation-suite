import time
from HeaderButton_Page import HeaderButtons
from BaseApp import highlight
from SocialNetworks_Page import SocialNetworks
from HomePage import HomePage
from Invoicefinancing_Pages import InvoiceFinancing
from ForTrade_Pages import ForTrade
from News_Pages import News
from ContactUs_Pages import ContactUs


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

    # close_live_chat = invoice_financing_page.close_live_chat_button()
    # close_live_chat.click()

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
    apply_finance_button = apply_finance.apply_for_finance_button_1()
    apply_finance_button.click()

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

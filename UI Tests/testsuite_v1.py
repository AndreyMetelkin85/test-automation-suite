import time
from selenium.webdriver.common.action_chains import ActionChains
from conftest import driver, slow_scroll

from framework.page_fixture_provider import home_page_fixture, articles_page_fixture, careers_page_fixture, \
    factoring_works_page_fixture, for_e_commerce_page_fixture, for_trade_page_fixture, contact_us_page_fixture, \
    glossary_page_fixture, header_buttons_fixture, invoice_financing_page_fixture, useful_guides_page_fixture, \
    partner_with_us_page_fixture, questions_answers_page_fixture, saas_page_fixture, social_networks_fixture, \
    revenue_based_financing_page_fixture


def test_buttons_in_header(
        driver, home_page_fixture, header_buttons_fixture, invoice_financing_page_fixture, saas_page_fixture,
        revenue_based_financing_page_fixture, for_trade_page_fixture, for_e_commerce_page_fixture,
        careers_page_fixture, articles_page_fixture, questions_answers_page_fixture, social_networks_fixture,
        factoring_works_page_fixture, useful_guides_page_fixture, contact_us_page_fixture, glossary_page_fixture,
        partner_with_us_page_fixture):

    accept_all_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_button.click()

    page_products_label = home_page_fixture.get_heading_label()
    assert page_products_label.is_displayed()

    page_header_buttons = header_buttons_fixture
    products_button = page_header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    financing_hover_button = page_header_buttons.financing_hover_button()
    actions.move_to_element(financing_hover_button[0])
    actions.click(financing_hover_button[0]).perform()

    page_invoice_financing = invoice_financing_page_fixture
    convert_label = page_invoice_financing.get_heading_label()
    assert convert_label.is_displayed()

    driver.back()

    page_header_buttons = header_buttons_fixture
    products_button = page_header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    financing_hover_button = page_header_buttons.financing_hover_button()
    actions.move_to_element(financing_hover_button[1])
    actions.click(financing_hover_button[1]).perform()

    page_revenue_based_financing = revenue_based_financing_page_fixture
    revenue_based_financing_label = page_revenue_based_financing.get_heading_label()
    assert revenue_based_financing_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_trade_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_trade_button[0])
    actions.click(for_trade_button[0]).perform()

    page_for_trade = for_trade_page_fixture
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_e_commerce_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_e_commerce_button[1])
    actions.click(for_e_commerce_button[1]).perform()

    page_for_trade = for_e_commerce_page_fixture
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_saas_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_saas_button[2])
    actions.click(for_saas_button[2]).perform()

    page_for_trade = saas_page_fixture
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    news_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(news_button[0])
    actions.click(news_button[0]).perform()

    page_news = articles_page_fixture
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    careers_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(careers_button[1])
    actions.click(careers_button[1]).perform()

    page_careers = careers_page_fixture
    careers_label = page_careers.get_heading_label()
    assert careers_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    faq_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(faq_button[2])
    actions.click(faq_button[2]).perform()

    page_faq = questions_answers_page_fixture
    faq_label = page_faq.get_heading_label()
    assert faq_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    useful_guides_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(useful_guides_button[3])
    actions.click(useful_guides_button[3]).perform()

    page_useful_guides = useful_guides_page_fixture
    useful_guides_label = page_useful_guides.get_heading_label()
    assert useful_guides_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    how_factoring_works_button = page_header_buttons.resources_hover_button_right()
    actions.move_to_element(how_factoring_works_button[0])
    actions.click(how_factoring_works_button[0]).perform()

    page_how_factoring_works = factoring_works_page_fixture
    how_factoring_works_label = page_how_factoring_works.get_heading_label()
    assert how_factoring_works_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    glossary_button = page_header_buttons.resources_hover_button_right()
    actions.move_to_element(glossary_button[1])
    actions.click(glossary_button[1]).perform()

    page_glossary = glossary_page_fixture
    glossary_label = page_glossary.get_heading_label()
    assert glossary_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    articles_button = page_header_buttons.resources_hover_button_right()
    actions.move_to_element(articles_button[2])
    actions.click(articles_button[2]).perform()

    page_news = articles_page_fixture
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    partner_with_us_button = page_header_button.partner_with_us_button()
    driver.execute_script("arguments[0].click();", partner_with_us_button)

    page_partner_with_us = partner_with_us_page_fixture
    partner_with_us_label = page_partner_with_us.get_heading_label()
    partner_with_us_label.is_displayed()

    driver.back()

    page_header_button = header_buttons_fixture
    contact_us_button = page_header_button.contact_us_button()
    driver.execute_script("arguments[0].click();", contact_us_button)

    page_news = contact_us_page_fixture
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()


def test_opening_social_networks(driver, slow_scroll, social_networks_fixture):
    home_page = social_networks_fixture

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    slow_scroll(driver, scroll_step=100, pause_duration=0.1)

    footer_logo = home_page.footer_logo_sten()
    assert footer_logo.is_displayed()

    linkedin_button = home_page.social_networks()
    linkedin_button[0].click()
    time.sleep(3)

    current_url = driver.current_url
    expected_url_prefix = "https://www.linkedin.com/company/stenn-financial-services"
    assert current_url.startswith(expected_url_prefix)

    driver.back()

    twitter_button = social_networks_fixture
    twitter_button.social_networks()[1].click()
    time.sleep(7)

    current_url = driver.current_url
    expected_url_prefix = "https://twitter.com/i/flow/login?redirect_after_login=%2FStenn_Intl"
    assert current_url.startswith(expected_url_prefix)

    driver.back()

    facebook_button = home_page.social_networks()
    facebook_button[2].click()
    time.sleep(2)

    current_url = driver.current_url
    expected_url_prefix = "https://www.facebook.com/StennIntl"
    assert current_url.startswith(expected_url_prefix)

    driver.back()

    youtube_button = social_networks_fixture
    youtube_button.social_networks()[3].click()
    time.sleep(2)

    current_url = driver.current_url
    expected_url = "https://www.youtube.com/channel/UCVsztAj0QmhKkfu4IKMHUOA"
    assert current_url == expected_url

    driver.back()


def test_apply_for_finance_button_clickability(driver, home_page_fixture):

    accept_all_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_button.click()

    app_for_finance_button = home_page_fixture.apply_for_finance_button()
    app_for_finance_button[0].click()
    time.sleep(0.5)

    invoice_financing_label = home_page_fixture.invoice_financing_label()
    assert invoice_financing_label.is_displayed()

    invoice_financing_label = home_page_fixture.revenue_based_financing_label()
    assert invoice_financing_label.is_displayed()

    driver.back()

    driver.execute_script("window.scrollBy(0, 900);")
    time.sleep(0.5)

    apply_finance_button = home_page_fixture.apply_for_finance_button()
    apply_finance_button[1].click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])

    current_url = driver.current_url
    expected_url = "https://app.stenn.com/auth/sign-up"
    assert current_url == expected_url


def test_what_is_stenn_block_button_navigation(driver, home_page_fixture, articles_page_fixture, careers_page_fixture,
                                               useful_guides_page_fixture, questions_answers_page_fixture):
    accept_all_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_button.click()

    driver.execute_script("window.scrollBy(0, 2600)")
    time.sleep(0.5)

    home_page_what_stenn_label = home_page_fixture.what_stenn_label()
    assert home_page_what_stenn_label[0].is_displayed()

    what_stenn_block_articles_button = home_page_fixture.what_stenn_button()
    what_stenn_block_articles_button[0].click()

    article_page = articles_page_fixture
    articles_read_more_button = article_page.get_heading_label()
    assert articles_read_more_button.is_displayed()

    driver.back()

    what_stenn_block_useful_guides_label = home_page_fixture.what_stenn_label()
    assert what_stenn_block_useful_guides_label[1].is_displayed()

    what_stenn_block_useful_guides_button = home_page_fixture.what_stenn_button()
    what_stenn_block_useful_guides_button[1].click()

    useful_guides_page = useful_guides_page_fixture
    useful_guides_label = useful_guides_page.get_heading_label()
    assert useful_guides_label.is_displayed()

    driver.back()

    what_stenn_block_careers_label = home_page_fixture.what_stenn_label()
    assert what_stenn_block_careers_label[2].is_displayed()

    what_stenn_block_careers_button = home_page_fixture.what_stenn_button()
    what_stenn_block_careers_button[2].click()

    careers_page = careers_page_fixture
    careers_label = careers_page.get_heading_label()
    assert careers_label.is_displayed()

    driver.back()

    what_stenn_block_faq_label = home_page_fixture.what_stenn_label()
    assert what_stenn_block_faq_label[3].is_displayed()

    what_stenn_block_faq_button = home_page_fixture.what_stenn_button()
    what_stenn_block_faq_button[3].click()

    faq_page = questions_answers_page_fixture
    faq_label = faq_page.get_heading_label()
    assert faq_label.is_displayed()


def test_opening_login_page(driver, header_buttons_fixture, home_page_fixture):

    accept_all_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_button.click()

    login_button = header_buttons_fixture.login_button()
    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()
    invoice_financing_button = header_buttons_fixture.login_dropdown()
    actions.move_to_element(invoice_financing_button[0])
    actions.click(invoice_financing_button[0]).perform()

    time.sleep(3)

    current_url = driver.current_url
    expected_prefix = 'https://app.stenn.com/auth/login'
    assert current_url.startswith(expected_prefix), f"URL {current_url} does not start with {expected_prefix}"

    driver.back()

    login_button = header_buttons_fixture.login_button()
    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()
    invoice_financing_button = header_buttons_fixture.login_dropdown()
    actions.move_to_element(invoice_financing_button[1])
    actions.click(invoice_financing_button[1]).perform()

    time.sleep(3)

    current_url = driver.current_url
    expected_url = "https://rbf.stenn.com/auth/login"
    assert current_url == expected_url


def test_select_your_finance_option(driver, home_page_fixture, header_buttons_fixture):

    accept_all_button = home_page_fixture.accept_all_pop_up_button()
    accept_all_button.click()

    apply_for_finance_button = header_buttons_fixture.apply_for_finance_button()
    driver.execute_script("arguments[0].click();", apply_for_finance_button[1])

    invoice_financing_label = home_page_fixture.invoice_financing_label()
    assert invoice_financing_label.is_displayed()

    invoice_financing_label = home_page_fixture.revenue_based_financing_label()
    assert invoice_financing_label.is_displayed()

    apply_for_finance_button = header_buttons_fixture.apply_for_finance_button()
    apply_for_finance_button[2].click()

    driver.switch_to.window(driver.window_handles[1])

    current_url = driver.current_url
    expected_url = "https://app.stenn.com/auth/sign-up"
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    apply_for_finance_button = header_buttons_fixture.apply_for_finance_button()
    apply_for_finance_button[3].click()

    driver.switch_to.window(driver.window_handles[2])

    current_url = driver.current_url
    expected_url = "https://rbf.stenn.com/auth/sign-up"
    assert current_url == expected_url

from selenium.webdriver.common.action_chains import ActionChains
from test_ui.conftest import driver, slow_scroll, wait, page_fixture


def test_buttons_in_header(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    page_products_label = page_fixture.home_page.get_heading_label()
    assert page_products_label.is_displayed()

    page_header_buttons = page_fixture.header_buttons
    products_button = page_header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    financing_hover_button = page_header_buttons.financing_hover_button()
    actions.move_to_element(financing_hover_button[0])
    actions.click(financing_hover_button[0]).perform()

    page_invoice_financing = page_fixture.invoice_financing_page
    convert_label = page_invoice_financing.get_heading_label()
    assert convert_label.is_displayed()

    driver.back()

    page_header_buttons = page_fixture.header_buttons
    products_button = page_header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    financing_hover_button = page_header_buttons.financing_hover_button()
    actions.move_to_element(financing_hover_button[1])
    actions.click(financing_hover_button[1]).perform()

    page_revenue_based_financing = page_fixture.revenue_based_financing_page
    revenue_based_financing_label = page_revenue_based_financing.get_heading_label()
    assert revenue_based_financing_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_trade_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_trade_button[0])
    actions.click(for_trade_button[0]).perform()

    page_for_trade = page_fixture.for_trade_page
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_e_commerce_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_e_commerce_button[1])
    actions.click(for_e_commerce_button[1]).perform()

    page_for_trade = page_fixture.for_e_commerce_page
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_saas_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_saas_button[2])
    actions.click(for_saas_button[2]).perform()

    page_for_trade = page_fixture.saas_page
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    news_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(news_button[0])
    actions.click(news_button[0]).perform()

    page_news = page_fixture.articles_page
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    careers_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(careers_button[1])
    actions.click(careers_button[1]).perform()

    page_careers = page_fixture.careers_page
    careers_label = page_careers.get_heading_label()
    assert careers_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    faq_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(faq_button[2])
    actions.click(faq_button[2]).perform()

    page_faq = page_fixture.questions_answers_page
    faq_label = page_faq.get_heading_label()
    assert faq_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    useful_guides_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(useful_guides_button[3])
    actions.click(useful_guides_button[3]).perform()

    page_useful_guides = page_fixture.useful_guides_page
    useful_guides_label = page_useful_guides.get_heading_label()
    assert useful_guides_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    how_factoring_works_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(how_factoring_works_button[4])
    actions.click(how_factoring_works_button[4]).perform()

    page_how_factoring_works = page_fixture.factoring_works_page
    how_factoring_works_label = page_how_factoring_works.get_heading_label()
    assert how_factoring_works_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    glossary_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(glossary_button[5])
    actions.click(glossary_button[5]).perform()

    page_glossary = page_fixture.glossary_page
    glossary_label = page_glossary.get_heading_label()
    assert glossary_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    articles_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(articles_button[6])
    actions.click(articles_button[6]).perform()

    page_news = page_fixture.articles_page
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    partner_with_us_button = page_header_button.partner_with_us_button()
    driver.execute_script("arguments[0].click();", partner_with_us_button)

    page_partner_with_us = page_fixture.partner_with_us_page
    partner_with_us_label = page_partner_with_us.get_heading_label()
    partner_with_us_label.is_displayed()

    driver.back()

    page_header_button = page_fixture.header_buttons
    contact_us_button = page_header_button.contact_us_button()
    driver.execute_script("arguments[0].click();", contact_us_button)

    contact_us_page = page_fixture.contact_us_page
    articles_label = contact_us_page.get_heading_label()
    assert articles_label.is_displayed()


def test_opening_social_networks(driver, slow_scroll, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    slow_scroll(driver, scroll_step=100, pause_duration=0.1)

    footer_logo = page_fixture.social_networks.footer_logo_sten()
    assert footer_logo.is_displayed()

    expected_urls = {
        "linkedin.com": "https://www.linkedin.com/company/stenn-financial-services",
        "twitter.com": "https://twitter.com/i/flow/login?redirect_after_login=%2FStenn_Intl",
        "facebook.com": "https://www.facebook.com/StennIntl",
        "youtube.com": "https://www.youtube.com/channel/UCVsztAj0QmhKkfu4IKMHUOA"
    }

    linkedin_button = page_fixture.social_networks.social_networks()
    linkedin_button[0].click()

    expected_url = expected_urls["linkedin.com"]
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.back()

    twitter_button = page_fixture.social_networks.social_networks()
    twitter_button[1].click()

    expected_url = expected_urls["twitter.com"]
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.back()
    driver.back()

    facebook_button = page_fixture.social_networks.social_networks()
    facebook_button[2].click()

    expected_url = expected_urls["facebook.com"]
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url.startswith(expected_url)

    driver.back()

    youtube_button = page_fixture.social_networks.social_networks()
    youtube_button[3].click()

    expected_url = expected_urls["youtube.com"]
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.back()


def test_apply_for_finance_button_clickability(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    app_for_finance_button = page_fixture.home_page.apply_for_finance_button()
    app_for_finance_button[0].click()

    invoice_financing_label = page_fixture.home_page.invoice_financing_label()
    assert invoice_financing_label.is_displayed()

    invoice_financing_label = page_fixture.home_page.revenue_based_financing_label()
    assert invoice_financing_label.is_displayed()

    driver.back()

    driver.execute_script("window.scrollBy(0, 900);")

    apply_finance_button = page_fixture.home_page.apply_for_finance_button()
    apply_finance_button[1].click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://app.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url


def test_what_is_stenn_block_button_navigation(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    driver.execute_script("window.scrollBy(0, 2600)")

    home_page_what_stenn_label = page_fixture.home_page.what_stenn_label()
    assert home_page_what_stenn_label[0].is_displayed()

    what_stenn_block_articles_button = page_fixture.home_page.what_stenn_button()
    what_stenn_block_articles_button[0].click()

    article_page_label = page_fixture.articles_page.get_heading_label()
    assert article_page_label.is_displayed()

    driver.back()

    what_stenn_block_useful_guides_label = page_fixture.home_page.what_stenn_label()
    assert what_stenn_block_useful_guides_label[1].is_displayed()

    what_stenn_block_useful_guides_button = page_fixture.home_page.what_stenn_button()
    what_stenn_block_useful_guides_button[1].click()

    useful_guides_label = page_fixture.useful_guides_page.get_heading_label()
    assert useful_guides_label.is_displayed()

    driver.back()

    what_stenn_block_careers_label = page_fixture.home_page.what_stenn_label()
    assert what_stenn_block_careers_label[2].is_displayed()

    what_stenn_block_careers_button = page_fixture.home_page.what_stenn_button()
    what_stenn_block_careers_button[2].click()

    careers_page_label = page_fixture.careers_page.get_heading_label()
    assert careers_page_label.is_displayed()

    driver.back()

    what_stenn_block_faq_label = page_fixture.home_page.what_stenn_label()
    assert what_stenn_block_faq_label[3].is_displayed()

    what_stenn_block_faq_button = page_fixture.home_page.what_stenn_button()
    what_stenn_block_faq_button[3].click()

    faq_page_label = page_fixture.questions_answers_page.get_heading_label()
    assert faq_page_label.is_displayed()


def test_opening_login_page(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    login_button = page_fixture.header_buttons.login_button()
    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()
    invoice_financing_button = page_fixture.header_buttons.login_dropdown()
    actions.move_to_element(invoice_financing_button[0])
    actions.click(invoice_financing_button[0]).perform()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = 'https://app.stenn.com/auth/sign-up'
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    login_button = page_fixture.header_buttons.login_button()
    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()
    invoice_financing_button = page_fixture.header_buttons.login_dropdown()
    actions.move_to_element(invoice_financing_button[1])
    actions.click(invoice_financing_button[1]).perform()

    driver.switch_to.window(driver.window_handles[2])

    expected_url = 'https://rbf.stenn.com/auth/sign-up'
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url


def test_select_your_finance_option(driver, page_fixture, wait):
    page_fixture.go_to_web_site_stenn.go_to_web_site_stenn()
    accept_all_cookies_button = page_fixture.home_page.accept_all_pop_up_button()
    accept_all_cookies_button.click()

    apply_for_finance_button = page_fixture.header_buttons.apply_for_finance_button()
    driver.execute_script("arguments[0].click();", apply_for_finance_button[1])

    invoice_financing_label = page_fixture.home_page.invoice_financing_label()
    assert invoice_financing_label.is_displayed()

    invoice_financing_label = page_fixture.home_page.revenue_based_financing_label()
    assert invoice_financing_label.is_displayed()

    apply_for_finance_button = page_fixture.header_buttons.apply_for_finance_button()
    apply_for_finance_button[2].click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://app.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

    driver.switch_to.window(driver.window_handles[0])

    apply_for_finance_button = page_fixture.header_buttons.apply_for_finance_button()
    apply_for_finance_button[3].click()

    driver.switch_to.window(driver.window_handles[2])

    expected_url = "https://rbf.stenn.com/auth/sign-up"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url

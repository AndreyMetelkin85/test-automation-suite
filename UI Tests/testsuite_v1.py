import time
from selenium.webdriver.common.action_chains import ActionChains
from framework.pages.website_stenn.articles_page import Articles
from framework.pages.website_stenn.careers_page import Careers
from framework.pages.website_stenn.factoring_works_page import FactoringWorks
from framework.pages.website_stenn.for_e_commerce_page import ForECommerce
from framework.pages.website_stenn.glossary_page import Glossary
from framework.pages.website_stenn.header_button_page import HeaderButtons

from framework.pages.website_stenn.partner_with_us_page import PartnerWithUs
from framework.pages.website_stenn.questions_answers_page import QuestionsAnswers
from framework.pages.website_stenn.revenue_based_financing_page import RevenueBasedFinancing
from framework.pages.website_stenn.saas_page import Saas
from framework.pages.website_stenn.social_networks_page import SocialNetworks
from framework.pages.website_stenn.home_page import HomePage
from framework.pages.website_stenn.invoice_financing_page import InvoiceFinancing
from framework.pages.website_stenn.for_trade_page import ForTrade
from framework.pages.website_stenn.contact_us_page import ContactUs
from framework.pages.website_stenn.finance_option_page import FinanceOption
from conftest import driver, slow_scroll
from framework.pages.website_stenn.useful_guides_page import UsefulGuides


def test_buttons_in_header(driver):
    home_page = HomePage(driver)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    page_products_label = home_page.get_heading_label()
    assert page_products_label.is_displayed()

    page_header_buttons = HeaderButtons(driver)
    products_button = page_header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    financing_hover_button = page_header_buttons.financing_hover_button()
    actions.move_to_element(financing_hover_button[0])
    actions.click(financing_hover_button[0]).perform()

    page_invoice_financing = InvoiceFinancing(driver)
    convert_label = page_invoice_financing.get_heading_label()
    assert convert_label.is_displayed()

    driver.back()

    page_header_buttons = HeaderButtons(driver)
    products_button = page_header_buttons.products_button()
    actions = ActionChains(driver)
    actions.move_to_element(products_button).perform()
    financing_hover_button = page_header_buttons.financing_hover_button()
    actions.move_to_element(financing_hover_button[1])
    actions.click(financing_hover_button[1]).perform()

    page_revenue_based_financing = RevenueBasedFinancing(driver)
    revenue_based_financing_label = page_revenue_based_financing.get_heading_label()
    assert revenue_based_financing_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_trade_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_trade_button[0])
    actions.click(for_trade_button[0]).perform()

    page_for_trade = ForTrade(driver)
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_e_commerce_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_e_commerce_button[1])
    actions.click(for_e_commerce_button[1]).perform()

    page_for_trade = ForECommerce(driver)
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    solutions_button = page_header_button.solutions_button()
    actions = ActionChains(driver)
    actions.move_to_element(solutions_button).perform()
    for_saas_button = page_header_buttons.solutions_hover_button()
    actions.move_to_element(for_saas_button[2])
    actions.click(for_saas_button[2]).perform()

    page_for_trade = Saas(driver)
    boost_your_cash_label = page_for_trade.get_heading_label()
    assert boost_your_cash_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    news_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(news_button[0])
    actions.click(news_button[0]).perform()

    page_news = Articles(driver)
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    careers_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(careers_button[1])
    actions.click(careers_button[1]).perform()

    page_careers = Careers(driver)
    careers_label = page_careers.get_heading_label()
    assert careers_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    faq_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(faq_button[2])
    actions.click(faq_button[2]).perform()

    page_faq = QuestionsAnswers(driver)
    faq_label = page_faq.get_heading_label()
    assert faq_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    useful_guides_button = page_header_buttons.resources_hover_button()
    actions.move_to_element(useful_guides_button[3])
    actions.click(useful_guides_button[3]).perform()

    page_useful_guides = UsefulGuides(driver)
    useful_guides_label = page_useful_guides.get_heading_label()
    assert useful_guides_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    how_factoring_works_button = page_header_buttons.resources_hover_button_right()
    actions.move_to_element(how_factoring_works_button[0])
    actions.click(how_factoring_works_button[0]).perform()

    page_how_factoring_works = FactoringWorks(driver)
    how_factoring_works_label = page_how_factoring_works.get_heading_label()
    assert how_factoring_works_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    glossary_button = page_header_buttons.resources_hover_button_right()
    actions.move_to_element(glossary_button[1])
    actions.click(glossary_button[1]).perform()

    page_glossary = Glossary(driver)
    glossary_label = page_glossary.get_heading_label()
    assert glossary_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    resources_button = page_header_button.resources_button()
    actions = ActionChains(driver)
    actions.move_to_element(resources_button).perform()
    articles_button = page_header_buttons.resources_hover_button_right()
    actions.move_to_element(articles_button[2])
    actions.click(articles_button[2]).perform()

    page_news = Articles(driver)
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    partner_with_us_button = page_header_button.partner_with_us_button()
    driver.execute_script("arguments[0].click();", partner_with_us_button)

    page_partner_with_us = PartnerWithUs(driver)
    partner_with_us_label = page_partner_with_us.get_heading_label()
    partner_with_us_label.is_displayed()

    driver.back()

    page_header_button = HeaderButtons(driver)
    contact_us_button = page_header_button.contact_us_button()
    driver.execute_script("arguments[0].click();", contact_us_button)

    page_news = ContactUs(driver)
    articles_label = page_news.get_heading_label()
    assert articles_label.is_displayed()


def test_opening_social_networks(driver, slow_scroll):
    home_page = SocialNetworks(driver)

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

    twitter_button = SocialNetworks(driver)
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

    youtube_button = SocialNetworks(driver)
    youtube_button.social_networks()[3].click()
    time.sleep(2)

    current_url = driver.current_url
    expected_url = "https://www.youtube.com/channel/UCVsztAj0QmhKkfu4IKMHUOA"
    assert current_url == expected_url

    driver.back()


def test_apply_for_finance_button_clickability(driver):
    home_page = HomePage(driver)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    app_for_finance_button = home_page.apply_for_finance_button()
    app_for_finance_button[0].click()
    time.sleep(0.5)

    invoice_financing_label = home_page.invoice_financing_label()
    assert invoice_financing_label.is_displayed()

    invoice_financing_label = home_page.revenue_based_financing_label()
    assert invoice_financing_label.is_displayed()

    driver.back()

    driver.execute_script("window.scrollBy(0, 900);")
    time.sleep(0.5)

    apply_finance_button = home_page.apply_for_finance_button()
    apply_finance_button[1].click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])

    current_url = driver.current_url
    expected_url = "https://app.stenn.com/auth/sign-up"
    assert current_url == expected_url


def test_what_is_stenn_block_button_navigation(driver):
    home_page = HomePage(driver)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    driver.execute_script("window.scrollBy(0, 2600)")
    time.sleep(0.5)

    home_page_what_stenn_label = home_page.what_stenn_label()
    assert home_page_what_stenn_label[0].is_displayed()

    what_stenn_block_articles_button = home_page.what_stenn_button()
    what_stenn_block_articles_button[0].click()

    article_page = Articles(driver)
    articles_read_more_button = article_page.get_heading_label()
    assert articles_read_more_button.is_displayed()

    driver.back()

    what_stenn_block_useful_guides_label = home_page.what_stenn_label()
    assert what_stenn_block_useful_guides_label[1].is_displayed()

    what_stenn_block_useful_guides_button = home_page.what_stenn_button()
    what_stenn_block_useful_guides_button[1].click()

    useful_guides_page = UsefulGuides(driver)
    useful_guides_label = useful_guides_page.get_heading_label()
    assert useful_guides_label.is_displayed()

    driver.back()

    what_stenn_block_careers_label = home_page.what_stenn_label()
    assert what_stenn_block_careers_label[2].is_displayed()

    what_stenn_block_careers_button = home_page.what_stenn_button()
    what_stenn_block_careers_button[2].click()

    careers_page = Careers(driver)
    careers_label = careers_page.get_heading_label()
    assert careers_label.is_displayed()

    driver.back()

    what_stenn_block_faq_label = home_page.what_stenn_label()
    assert what_stenn_block_faq_label[3].is_displayed()

    what_stenn_block_faq_button = home_page.what_stenn_button()
    what_stenn_block_faq_button[3].click()

    faq_page = QuestionsAnswers(driver)
    faq_label = faq_page.get_heading_label()
    assert faq_label.is_displayed()


def test_opening_login_page(driver):
    home_page = HeaderButtons(driver)

    login_button = home_page.login_dropdown()
    login_button.click()
    invoice_financing_button = home_page.invoice_fincace_button()
    invoice_financing_button.is_displayed()
    revenue_button = home_page.revenue_button()
    revenue_button.is_displayed()

    invoice_financing_button.click()
    current_url = driver.current_url
    expected_url = "https://app.stenn.com/auth/login"
    assert current_url == expected_url

    driver.back()
    time.sleep(0.5)

    login_button = home_page.login_dropdown()
    login_button.click()

    revenue_button = home_page.revenue_button()
    revenue_button.click()
    current_url = driver.current_url
    expected_url = "https://rbf.stenn.com/auth/login"
    assert current_url == expected_url

    driver.back()
    time.sleep(0.5)


def test_select_your_finance_option(driver):
    open_page = HeaderButtons(driver)

    home_page = HomePage(driver)
    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    apply_for_finance_button = open_page.apply_for_finance_button()
    apply_for_finance_button.click()

    select_finance_option_page = FinanceOption(driver)
    select_finance_option_heading = select_finance_option_page.get_heading_label()
    assert select_finance_option_heading.is_displayed()

    international_domestic_financing = select_finance_option_page.international_and_domestic_label()
    international_domestic_financing.is_displayed()

    apply_for_finance_app = select_finance_option_page.apply_for_finance_app()
    apply_for_finance_app.click()

    current_url = driver.current_url
    expected_url = "https://app.stenn.com/auth/sign-up"
    assert current_url == expected_url

    driver.back()

    revenue_based_financing_label = select_finance_option_page.revenue_based_financing_label()
    revenue_based_financing_label.is_displayed()

    apply_for_finance_rbf = select_finance_option_page.apply_for_finance_rbf()
    apply_for_finance_rbf.click()

    current_url = driver.current_url
    expected_url = "https://rbf.stenn.com/auth/sign-up"
    assert current_url == expected_url

    driver.back()

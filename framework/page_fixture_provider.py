import pytest

from framework.pages.website_stenn.articles_page import Articles
from framework.pages.website_stenn.careers_page import Careers
from framework.pages.website_stenn.contact_us_page import ContactUs
from framework.pages.website_stenn.factoring_works_page import FactoringWorks
from framework.pages.website_stenn.finance_option_page import FinanceOption
from framework.pages.website_stenn.for_e_commerce_page import ForECommerce
from framework.pages.website_stenn.for_trade_page import ForTrade
from framework.pages.website_stenn.glossary_page import Glossary
from framework.pages.website_stenn.header_button_page import HeaderButtons
from framework.pages.website_stenn.home_page import HomePage
from framework.pages.website_stenn.invoice_financing_page import InvoiceFinancing
from framework.pages.website_stenn.news_page import News
from framework.pages.website_stenn.partner_with_us_page import PartnerWithUs
from framework.pages.website_stenn.questions_answers_page import QuestionsAnswers
from framework.pages.website_stenn.resources_page import Resources
from framework.pages.website_stenn.revenue_based_financing_page import RevenueBasedFinancing
from framework.pages.website_stenn.saas_page import Saas
from framework.pages.website_stenn.social_networks_page import SocialNetworks
from framework.pages.website_stenn.useful_guides_page import UsefulGuides


@pytest.fixture
def home_page_fixture(driver):
    home_page = HomePage(driver)
    return home_page


@pytest.fixture
def articles_page_fixture(driver):
    articles_page = Articles(driver)
    return articles_page


@pytest.fixture
def careers_page_fixture(driver):
    careers_page = Careers(driver)
    return careers_page


@pytest.fixture
def contact_us_page_fixture(driver):
    contact_us_page = ContactUs(driver)
    return contact_us_page


@pytest.fixture
def factoring_works_page_fixture(driver):
    factoring_works_page = FactoringWorks(driver)
    return factoring_works_page


@pytest.fixture
def finance_option_page_fixture(driver):
    finance_option_page = FinanceOption(driver)
    return finance_option_page


@pytest.fixture
def for_e_commerce_page_fixture(driver):
    for_e_commerce_page = ForECommerce(driver)
    return for_e_commerce_page


@pytest.fixture
def for_trade_page_fixture(driver):
    for_trade_page = ForTrade(driver)
    return for_trade_page


@pytest.fixture
def glossary_page_fixture(driver):
    glossary_page = Glossary(driver)
    return glossary_page


@pytest.fixture
def header_buttons_fixture(driver):
    header_buttons = HeaderButtons(driver)
    return header_buttons


@pytest.fixture
def invoice_financing_page_fixture(driver):
    invoice_financing_page = InvoiceFinancing(driver)
    return invoice_financing_page


@pytest.fixture
def news_page_fixture(driver):
    news_page = News(driver)
    return news_page


@pytest.fixture
def partner_with_us_page_fixture(driver):
    partner_with_us_page = PartnerWithUs(driver)
    return partner_with_us_page


@pytest.fixture
def questions_answers_page_fixture(driver):
    questions_answers_page = QuestionsAnswers(driver)
    return questions_answers_page


@pytest.fixture
def resources_page_fixture(driver):
    resources_page = Resources(driver)
    return resources_page


@pytest.fixture
def revenue_based_financing_page_fixture(driver):
    revenue_based_financing_page = RevenueBasedFinancing(driver)
    return revenue_based_financing_page


@pytest.fixture
def saas_page_fixture(driver):
    saas_page = Saas(driver)
    return saas_page


@pytest.fixture
def social_networks_fixture(driver):
    social_networks = SocialNetworks(driver)
    return social_networks


@pytest.fixture
def useful_guides_page_fixture(driver):
    useful_guides_page = UsefulGuides(driver)
    return useful_guides_page

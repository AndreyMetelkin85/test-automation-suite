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


class PageFixture:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.articles_page = Articles(driver)
        self.careers_page = Careers(driver)
        self.contact_us_page = ContactUs(driver)
        self.factoring_works_page = FactoringWorks(driver)
        self.finance_option_page = FinanceOption(driver)
        self.for_e_commerce_page = ForECommerce(driver)
        self.for_trade_page = ForTrade(driver)
        self.glossary_page = Glossary(driver)
        self.header_buttons = HeaderButtons(driver)
        self.invoice_financing_page = InvoiceFinancing(driver)
        self.news_page = News(driver)
        self.partner_with_us_page = PartnerWithUs(driver)
        self.questions_answers_page = QuestionsAnswers(driver)
        self.resources_page = Resources(driver)
        self.revenue_based_financing_page = RevenueBasedFinancing(driver)
        self.saas_page = Saas(driver)
        self.social_networks = SocialNetworks(driver)
        self.useful_guides_page = UsefulGuides(driver)

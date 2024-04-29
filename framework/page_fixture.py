from base_page import BasePage
from framework.website_stenn_page.articles_page import Articles
from framework.website_stenn_page.careers_page import Careers
from framework.website_stenn_page.contact_us_page import ContactUs
from framework.website_stenn_page.factoring_works_page import FactoringWorks
from framework.website_stenn_page.finance_option_page import FinanceOption
from framework.website_stenn_page.for_e_commerce_page import ForECommerce
from framework.website_stenn_page.for_trade_page import ForTrade
from framework.website_stenn_page.glossary_page import Glossary
from framework.website_stenn_page.header_button_page import HeaderButtons
from framework.website_stenn_page.home_page import HomePage
from framework.website_stenn_page.invoice_financing_page import InvoiceFinancing
from framework.website_stenn_page.news_page import News
from framework.website_stenn_page.partner_with_us_page import PartnerWithUs
from framework.website_stenn_page.questions_answers_page import QuestionsAnswers
from framework.website_stenn_page.resources_page import Resources
from framework.website_stenn_page.revenue_based_financing_page import RevenueBasedFinancing
from framework.website_stenn_page.saas_page import Saas
from framework.website_stenn_page.social_networks_page import SocialNetworks
from framework.website_stenn_page.useful_guides_page import UsefulGuides
from framework.toils_qa_page.demo_qa_home_page import ToolsQaHome
from framework.toils_qa_page.text_box_page import TextBox


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
        self.demo_qa_home_page = ToolsQaHome(driver)
        self.text_box_page = TextBox(driver)
        self.go_to_web_site_stenn = BasePage(driver)
        self.go_to_web_site_demo_qa = BasePage(driver)

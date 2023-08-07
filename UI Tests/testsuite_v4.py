import time
from header_button_page import HeaderButtons
from base_page import highlight
from news_page import News
from resources_page import Resources
from careers_page import Careers
from questions_answers_page import QuestionsAnswers
from factoring_works_page import FactoringWorks
from glossary_page import Glossary
from articles_page import Articles
from useful_guides_page import UsefulGuides
from collections import namedtuple

Page = namedtuple('Page', ['page_name', 'is_need_to_go_back'])


def test_buttons_header(driver):
    home_page = HeaderButtons(driver)

    resources_button = home_page.resources_button()
    resources_button.click()

    resources_page = Resources(driver)

    pages = [
        Page(News, False),
        Page(Careers, True),
        Page(QuestionsAnswers, False),
        Page(UsefulGuides, False),
        Page(FactoringWorks, False),
        Page(Glossary, False),
        Page(Articles, False)
    ]

    for index, current_page in enumerate(pages):
        resources_page.list_title_buttons()[index].click()
        page = current_page.page_name(driver)
        time.sleep(0.5)
        heading_label = page.get_heading_label()
        assert heading_label.is_displayed()
        if current_page.is_need_to_go_back:
            driver.back()
            time.sleep(1)


def test_blog_list_buttons(driver):
    home_page = HeaderButtons(driver)

    resources_button = home_page.resources_button()
    resources_button.click()

    resources_page = Resources(driver)
    resources_blog_list = resources_page.blog_titles_buttons()
    resources_blog_list[0].click()

    current_url = driver.current_url
    expected_url = "https://stenn.com/resources/articles/all/page-1"
    assert current_url == expected_url

    resources_page = Resources(driver)
    resources_blog_list = resources_page.blog_titles_buttons()
    resources_blog_list[1].click()

    current_url = driver.current_url
    expected_url = "https://stenn.com/resources/articles/news/page-1"
    assert current_url == expected_url

    resources_page = Resources(driver)
    resources_blog_list = resources_page.blog_titles_buttons()
    resources_blog_list[2].click()

    current_url = driver.current_url
    expected_url = "https://stenn.com/resources/articles/page-1"
    assert current_url == expected_url

    resources_page = Resources(driver)
    resources_blog_list = resources_page.blog_titles_buttons()
    resources_blog_list[3].click()

    current_url = driver.current_url
    expected_url = "https://stenn.com/resources/articles/press-releases/page-1"
    assert current_url == expected_url


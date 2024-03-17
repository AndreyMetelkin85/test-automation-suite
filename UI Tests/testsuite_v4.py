import time
from framework.pages.website_stenn.header_button_page import header_buttons_fixture
from framework.pages.website_stenn.news_page import News
from framework.pages.website_stenn.resources_page import Resources
from framework.pages.website_stenn.careers_page import careers_page_fixture
from framework.pages.website_stenn.questions_answers_page import questions_answers_page_fixture
from framework.pages.website_stenn.factoring_works_page import factoring_works_page_fixture
from framework.pages.website_stenn.glossary_page import glossary_page_fixture
from framework.pages.website_stenn.articles_page import articles_page_fixture
from framework.pages.website_stenn.useful_guides_page import useful_guides_page_fixture
from collections import namedtuple
from conftest import driver

Page = namedtuple('Page', ['page_name', 'is_need_to_go_back'])


def test_buttons_header(driver):
    home_page = header_buttons_fixture(driver)

    resources_button = home_page.resources_button()
    resources_button.click()

    resources_page = Resources(driver)

    pages = [
        Page(News, False),
        Page(careers_page_fixture, True),
        Page(questions_answers_page_fixture, False),
        Page(useful_guides_page_fixture, False),
        Page(factoring_works_page_fixture, False),
        Page(glossary_page_fixture, False),
        Page(articles_page_fixture, False)
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
    home_page = header_buttons_fixture(driver)

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


def test_careers_page(driver):
    home_page = header_buttons_fixture(driver)

    accept_all_button = home_page.accept_all_pop_up_button()
    accept_all_button.click()

    resources_button = home_page.resources_button()
    resources_button.click()

    resources_page = Resources(driver)
    careers_buttons = resources_page.list_title_buttons()
    careers_buttons[1].click()

    careers_page = careers_page_fixture(driver)
    careers_page_header_label = careers_page.get_heading_label()
    assert careers_page_header_label.is_displayed()

    view_openings_button = careers_page.view_openings_button()
    view_openings_button[0].click()

    current_url = driver.current_url
    expected_url = "https://boards.eu.greenhouse.io/stenn"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

    why_join_stenn_headline = careers_page.why_join_stenn()
    assert why_join_stenn_headline.is_displayed()

    why_join_stenn_subheadings = careers_page.why_join_stenn_subheadings()
    assert all(map(lambda subheading: subheading.is_displayed(), why_join_stenn_subheadings))

    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)

    view_openings_button = careers_page.view_openings_button()
    view_openings_button[1].click()

    current_url = driver.current_url
    expected_url = "https://boards.eu.greenhouse.io/stenn"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 1900);")
    time.sleep(1)

    making_difference_label = careers_page.making_difference_label()
    assert making_difference_label

    driver.execute_script("window.scrollBy(0, 1500);")
    time.sleep(1)

    culture_belonging_header = careers_page.culture_belonging_label()
    assert culture_belonging_header

    view_openings_button = careers_page.view_openings_button()
    view_openings_button[2].click()

    current_url = driver.current_url
    expected_url = "https://boards.eu.greenhouse.io/stenn"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 4100);")
    time.sleep(2)

    life_stenn_header = careers_page.life_at_stenn_label()
    assert life_stenn_header

    view_openings_button = careers_page.view_openings_button()
    view_openings_button[3].click()

    current_url = driver.current_url
    expected_url = "https://boards.eu.greenhouse.io/stenn"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 4800);")
    time.sleep(2)

    met_leadership_team_header = careers_page.leadership_team_label()
    assert met_leadership_team_header

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    view_openings_button = careers_page.view_openings_button()
    view_openings_button[4].click()

    current_url = driver.current_url
    expected_url = "https://boards.eu.greenhouse.io/stenn"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 5900);")
    time.sleep(2)

    our_values_guide_header = careers_page.our_values_guide_label()
    assert our_values_guide_header

    driver.execute_script("window.scrollBy(0, 260);")
    time.sleep(2)

    our_values_guide_subheadings = careers_page.our_values_guide_subheadings()
    assert all(map(lambda subheading: subheading.is_displayed(), our_values_guide_subheadings))

    driver.execute_script("window.scrollBy(0, 270);")
    time.sleep(2)

    view_openings_button = careers_page.view_openings_button()
    view_openings_button[5].click()

    current_url = driver.current_url
    expected_url = "https://boards.eu.greenhouse.io/stenn"
    assert current_url == expected_url

    driver.back()
    time.sleep(1)

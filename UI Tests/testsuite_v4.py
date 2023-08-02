import time
from header_button_page import HeaderButtons
from base_page import highlight
from resources_page import Resources
from careers_page import Careers
from questions_answers_page import QuestionsAnswers
from factoring_works_page import FactoringWorks
from glossary_page import Glossary
from articles_page import Articles
from useful_guides_page import UsefulGuides


def test_buttons_header(driver):
    home_page = HeaderButtons(driver)

    resources_button = home_page.resources_button()
    resources_button.click()

    resources_page = Resources(driver)
    articles_label = resources_page.news_heading_label()
    assert articles_label.is_displayed()
    highlight(articles_label)

    news_label = resources_page.blog_titles_buttons()
    assert news_label[1].is_displayed()
    highlight(news_label[1])

    count_buttons = 6
    for button in range(count_buttons):
        resources_list_button = resources_page.list_title_buttons()
        resources_list_button[button].click()
        time.sleep(1)
        if button == 1:
            careers_page = Careers(driver)
            careers_label = careers_page.join_stenn_heading_label()
            assert careers_label.is_displayed()
            highlight(careers_label)
            driver.back()
        elif button == 2:
            questions_answers_page = QuestionsAnswers(driver)
            questions_answers_label = questions_answers_page.questions_answers_heading_label()
            assert questions_answers_label.is_displayed()
            highlight(questions_answers_label)
        elif button == 3:
            useful_guides_page = UsefulGuides(driver)
            useful_guides_label = useful_guides_page.useful_guides_heading_label()
            assert useful_guides_label.is_displayed()
            highlight(useful_guides_label)
        elif button == 4:
            how_factoring_works_page = FactoringWorks(driver)
            how_factoring_works_label = how_factoring_works_page.factoring_works_heading_label()
            assert how_factoring_works_label.is_displayed()
            highlight(how_factoring_works_label)
        elif button == 5:
            glossary_page = Glossary(driver)
            glossary_label = glossary_page.glossary_heading_label()
            assert glossary_label.is_displayed()
            highlight(glossary_label)
        elif button == 6:
            articles_page = Articles(driver)
            articles_label = articles_page.articles_heading_label()
            assert articles_label.is_displayed()
            highlight(articles_label)

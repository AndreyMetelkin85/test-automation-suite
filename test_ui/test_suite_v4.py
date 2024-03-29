from conftest import driver, wait, page_fixture


def test_navigation_buttons_clickability(driver, wait, page_fixture):
    driver.get('https://www.stenn.com/resources/articles/news')

    pages = {
        1: (page_fixture.careers_page, "Join Stenn"),
        2: (page_fixture.questions_answers_page, "Questions & Answers"),
        3: (page_fixture.useful_guides_page, "Useful Guides"),
        4: (page_fixture.factoring_works_page, "Everything You Need to Know About Invoice Financing/ Factoring"),
        5: (page_fixture.glossary_page, "Glossary"),
        6: (page_fixture.articles_page, "Articles")
    }

    for button_index, (page, expected_heading) in pages.items():
        button_click = page_fixture.resources_page.list_resource_buttons()[button_index]
        button_click.click()

        heading_label = wait.wait_until_the_element_is_visible(page.get_heading_label())
        assert heading_label.text == expected_heading
        driver.back()

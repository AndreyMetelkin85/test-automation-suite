import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from framework.pages.website_stenn.main_page import MainPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    base_page = MainPage(driver)
    base_page.go_to_site()
    yield driver
    driver.quit()


@pytest.fixture
def slow_scroll():
    def scroll(driver, scroll_step=150, pause_duration=0.3):
        current_position = driver.execute_script('return window.pageYOffset')
        page_height = driver.execute_script('return document.body.scrollHeight')

        while current_position < page_height:
            current_position += scroll_step
            driver.execute_script(f'window.scrollTo(0, {current_position})')
            time.sleep(pause_duration)

    return scroll

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

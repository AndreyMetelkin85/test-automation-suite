class Config:
    BASE_URL = "https://stenn.com/"
    TIMEOUT = 2


def highlight(element):
    driver = element._parent
    driver.execute_script("arguments[0].style.border='5px solid blue'", element)

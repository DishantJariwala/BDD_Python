from selenium import webdriver


class Browser(object):

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)

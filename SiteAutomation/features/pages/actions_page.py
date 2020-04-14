from features.browser import Browser
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time


class AllActions(Browser):

    def navigate(self, url):
        self.driver.get(url)

    def timer_sleep(self, t):
        time.sleep(t)

    def close_window(self):
        self.driver.close()

    def click_element(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def input_data(self, locator, message):
        self.driver.find_element_by_xpath(locator).send_keys(message)

    def drag_drop(self, fromElements, toElements):
        fromElement = self.driver.find_element_by_xpath(fromElements)
        toElement = self.driver.find_element_by_xpath(toElements)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(fromElement, toElement).perform()

    def get_page_title(self):
        return self.driver.title

    def resize(self, fromElements):
        fromElement = self.driver.find_element_by_xpath(fromElements)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(fromElement, 150, 250).perform()

    def alert_handler(self):
        self.driver.switch_to.alert.accept()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,1000)", "")

    def select_by_val(self, locator, value):
        element = self.driver.find_element_by_xpath(locator)
        sel = Select(element)
        sel.select_by_value(value)

    def double_click(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def right_click(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        actions = ActionChains(self.driver)
        actions.context_click(element)

    def mouse_hover(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)

from features.browser import Browser
import time


class NewWindowActions(Browser):

    # New Browser Window

    def switch_window_1(self):
        parentHandle = self.driver.current_window_handle
        handles = self.driver.window_handles

        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)

        self.driver.maximize_window()
        self.driver.find_element_by_xpath(
            "/html//div[@id='main']/div[@class='wf-wrap']/div[@class='wf-container-main']/main[@role='main']/section/div[1]/div//a[@href='https://www.toolsqa.com/python-tutorial/']/img[@alt='Python Tutorial']").click()
        self.driver.find_element_by_xpath(
            "/html//div[@id='content']/div[1]/div[2]/div[@class='vc_column-inner']/div/div/div[@class='wpb_wrapper']/ul[2]//a[@href='https://www.toolsqa.com/python/python-print-function/']").click()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(parentHandle)

    # New Message Window
    # New Browser Tab
    # New DemoQA Window
    def switch_window_2(self):
        parentHandle = self.driver.current_window_handle
        handles = self.driver.window_handles

        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)

        self.driver.maximize_window()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(parentHandle)


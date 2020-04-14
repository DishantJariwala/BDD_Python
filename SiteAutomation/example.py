from selenium import webdriver
import time
from selenium.webdriver import ActionChains

_date_picker = "/html//input[@id='datepicker']"
_date_select = "//div[@id='ui-datepicker-div']/table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[5]/a[@href='#']"

driver = webdriver.Firefox()
actions = ActionChains(driver)

driver.get('https://demoqa.com/datepicker/')

driver.find_element_by_xpath(_date_picker).click()
time.sleep(3)
driver.find_element_by_xpath(_date_select).click()
time.sleep(5)

driver.close()

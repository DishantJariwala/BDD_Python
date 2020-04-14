from selenium import webdriver
from features.browser import Browser
from features.pages.actions_page import AllActions
from features.pages.new_window_page import NewWindowActions


def before_all(context):

    context.browser = Browser()
    # browser = Browser.browser_type(context.config.userdata['browser'])
    # context.browser = browser
    context.actions_page = AllActions()
    context.new_window_page = NewWindowActions()
    # def after_all(context):
    # context.browser.close()

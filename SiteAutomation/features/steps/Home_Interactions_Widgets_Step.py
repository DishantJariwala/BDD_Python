from behave import *
from nose.tools import *


# Home Page Action
@given(u'I navigate to the DEMO_QA HomePage')
def step_impl(context):
    context.actions_page.navigate("https://demoqa.com/")
    assert_equal(context.actions_page.get_page_title(),
                 "ToolsQA – Demo Website to Practice Automation – Demo Website to Practice Automation")


# Interaction Page Action
@when(u'I click on Interactions')
def step_impl(context):
    context.actions_page.click_element("//ul[@id='menu-top']//a[@title='Interactions']")


# Interaction Page Validation
@then(u'I am taken to the Interactions Page List')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Interactions – ToolsQA – Demo Website to Practice Automation")


# Widget Page Action
@given(u'I click on Widgets')
def step_impl(context):
    context.actions_page.click_element("//ul[@id='menu-top']//a[@title='Widgets']")


@then(u'I am taken to the Widgets Page List is Performed')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Widgets – ToolsQA – Demo Website to Practice Automation")

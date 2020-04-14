from behave import *
from nose.tools import *


# Sortable Action
@given(u'I navigate to Sortable link from InteractionPage')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/sortable/']")


@when(u'I perform Sortable Operations')
def step_impl(context):
    fromElement = "//ul[@id='sortable']/li[1]"
    toElement = "//ul[@id='sortable']/li[3]"
    context.actions_page.drag_drop(fromElement, toElement)
    context.actions_page.drag_drop(fromElement, toElement)


@then(u'I am on Sortable page and Sortable operations are performed')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Sortable – ToolsQA – Demo Website to Practice Automation")


# Selectable Action
@given(u'I navigate to Selectable link from InteractionPage')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/selectable/']")


@when(u'I perform Selectable Operations')
def step_impl(context):
    context.actions_page.click_element("//ol[@id='selectable']/li[.='Item 1']")
    context.actions_page.click_element("//ol[@id='selectable']/li[.='Item 2']")
    context.actions_page.click_element("//ol[@id='selectable']/li[.='Item 3']")
    context.actions_page.click_element("//ol[@id='selectable']/li[.='Item 4']")


@then(u'I am on Selectable page and Selectable operations are performed')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Selectable – ToolsQA – Demo Website to Practice Automation")


# Resizeable Action

@given(u'I navigate to Resizeable link from InteractionPage')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/resizable/']")


@when(u'I perform Resizeable Operations')
def step_impl(context):
    Element = "//div[@id='resizable']/div[3]"
    context.actions_page.resize(Element)


@then(u'I am on Resizeable page and Resizeable operations are performed')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Resizable – ToolsQA – Demo Website to Practice Automation")


# Droppable Action

@given(u'I navigate to Droppable link from InteractionPage')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/droppable/']")


@when(u'I perform Droppable Operations')
def step_impl(context):
    fromElement = "//div[@id='draggable']/p[.='Drag me to my target']"
    toElement = "/html//div[@id='droppable']"
    context.actions_page.drag_drop(fromElement, toElement)


@then(u'I am on Droppable page and Droppable operations are performed')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Droppable – ToolsQA – Demo Website to Practice Automation")


# Draggable Action
@given(u'I navigate to Draggable link from InteractionPage')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/draggable/']")


@when(u'I perform Draggable Operations')
def step_impl(context):
    fromElement = "/html//div[@id='draggable']"
    context.actions_page.resize(fromElement)


@then(u'I am on Draggable page and Draggable operations are performed')
def step_impl(context):
    assert_equal(context.actions_page.get_page_title(), "Draggable – ToolsQA – Demo Website to Practice Automation")

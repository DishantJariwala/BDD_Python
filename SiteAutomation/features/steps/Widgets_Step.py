from behave import *


########################################################################################################################


@given(u'I click on Automation Practice Switch')
def step_impl(context):
    context.actions_page.click_element(
        "//div[@id='content']//ul//a[@href='https://demoqa.com/automation-practice-switch-windows-2/']")


@then(u'Operations open is Performed')
def step_impl(context):
    print("Automation Practice Switch is Open")


########################################################################################################################


@given(u'I click on New Browser Window')
def step_impl(context):
    context.actions_page.click_element("/html//button[@id='button1']")


@then(u'New Browser Window Operation is Performed')
def step_impl(context):
    context.new_window_page.switch_window_1()


########################################################################################################################


@given(u'I click on New Message Window')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//button[.='New Message Window']")


@then(u'Open New Message Window and perform Operation is Performed')
def step_impl(context):
    context.new_window_page.switch_window_2()


########################################################################################################################


@given(u'I click on New Browser Tab')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//button[.='New Browser Tab']")


@then(u'Open New Browser Tab nd perform Operation is Performed')
def step_impl(context):
    context.new_window_page.switch_window_2()


########################################################################################################################


@given(u'I click on New DemoQA Window')
def step_impl(context):
    context.actions_page.click_element("/html//div[@id='content']//a[@href='https://demoqa.com/']")


@then(u'open New DemoQA Window and perform Operation is Performed')
def step_impl(context):
    context.new_window_page.switch_window_2()


########################################################################################################################


@given(u'I click on JavaScript Alert')
def step_impl(context):
    context.actions_page.click_element("/html//button[@id='alert']")


@then(u'interact with Alert Pop-Up is Performed')
def step_impl(context):
    context.actions_page.timer_sleep(5)
    context.actions_page.alert_handler()


########################################################################################################################


@given(u'I click on Go back to Widgets List')
def step_impl(context):
    context.actions_page.click_element("//ul[@id='menu-top']//a[@title='Widgets']")


########################################################################################################################


@given(u'I click on Automation Practice Table')
def step_impl(context):
    context.actions_page.click_element(
        "//div[@id='content']//ul//a[@href='https://demoqa.com/automation-practice-table/']")


@then(u'Automation Table Operations Open is Performed')
def step_impl(context):
    print("Automation Table Page is Open")


########################################################################################################################


@given(u'I click on Table Details')
def step_impl(context):
    context.actions_page.click_element(
        "/html//div[@id='content']//table[@class='tsc_table_s13']/tbody/tr[1]/td[6]/a[@href='#']")
    context.actions_page.timer_sleep(3)
    context.actions_page.click_element(
        "/html//div[@id='content']//table[@class='tsc_table_s13']/tbody/tr[3]/td[6]/a[@href='#']")


@then(u'Table Details Operation is Performed')
def step_impl(context):
    print("Table Operations Performed")


########################################################################################################################


@given(u'I click on Automation Practice Form')
def step_impl(context):
    context.actions_page.click_element(
        "//div[@id='content']//ul//a[@href='https://demoqa.com/automation-practice-form/']")


@then(u'All the Automation Practice Form Operations is Performed')
def step_impl(context):
    # locators
    _first_name = "/html//div[@id='content']//form[@class='form-horizontal']//input[@name='firstname']"
    _last_name = "/html//input[@id='lastname']"

    # actions
    context.actions_page.input_data(_first_name, "Dishant")
    context.actions_page.input_data(_last_name, "Jariwala")
    context.actions_page.scroll_down()
    context.actions_page.click_element(
        "/html//div[@id='content']//form[@class='form-horizontal']/fieldset/div[14]/input[1]")
    context.actions_page.click_element(
        "/html//div[@id='content']//form[@class='form-horizontal']/fieldset/div[18]/input[1]")
    context.actions_page.click_element(
        "/html//div[@id='content']//form[@class='form-horizontal']/fieldset/div[29]/input[3]")
    context.actions_page.select_by_val("/html//select[@id='continents']", "AF")


########################################################################################################################


@given(u'I click on Keyboard Events')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/keyboard-events/']")


@then(u'All Keyboard Events Operations is Performed')
def step_impl(context):
    # locator
    _file_path = "/html//input[@id='browseFile']"
    _file_location = "C:\\Users\\Dishant Jariwala\\Downloads\\geckodriver-v0.26.0-win64.zip"
    context.actions_page.input_data(_file_path, _file_location)
    context.actions_page.click_element("/html//button[@id='uploadButton']")
    context.actions_page.timer_sleep(3)
    context.actions_page.alert_handler()


########################################################################################################################


@given(u'I click on Tool Tip and Double Click')
def step_impl(context):
    context.actions_page.click_element(
        "//div[@id='content']//ul//a[@href='https://demoqa.com/tooltip-and-double-click/']")


@then(u'All ToolTip and DoubleClick Operations is Performed')
def step_impl(context):
    context.actions_page.double_click("/html//button[@id='doubleClickBtn']")
    context.actions_page.timer_sleep(3)
    context.actions_page.alert_handler()


########################################################################################################################


# locators
_date_picker = "/html//input[@id='datepicker']"
_date_back = "//div[@id='ui-datepicker-div']//a[@title='Prev']/span[@class='ui-icon ui-icon-circle-triangle-w']"
_date_select = "//div[@id='ui-datepicker-div']/table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[4]/a[@href='#']"


@given(u'I click on Date Picker')
def step_impl(context):
    context.actions_page.click_element("//div[@id='content']//ul//a[@href='https://demoqa.com/datepicker/']")


@then(u'DatePicker Operation is Performed')
def step_impl(context):
    context.actions_page.click_element(_date_picker)
    for i in range(6):
        context.actions_page.double_click(_date_back)
    context.actions_page.timer_sleep(3)
    context.actions_page.click_element(_date_select)


########################################################################################################################


@given(u'I click on Home')
def step_impl(context):
    context.actions_page.click_element("//ul[@id='menu-top']//a[@title='Home']")


@then(u'Exit The Browser is Performed')
def step_impl(context):
    context.actions_page.close_window()


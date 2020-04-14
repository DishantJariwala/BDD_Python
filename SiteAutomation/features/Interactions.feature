Feature: Interactions Automation


  Scenario: Go to DEMO_QA site
    Given I navigate to the DEMO_QA HomePage
    When I click on Interactions
    Then I am taken to the Interactions Page List

  Scenario: Go to Sortable
    Given I navigate to Sortable link from InteractionPage
    When I perform Sortable Operations
    Then I am on Sortable page and Sortable operations are performed

  Scenario: Go to DEMO_QA site
    Given I navigate to the DEMO_QA HomePage
    When I click on Interactions
    Then I am taken to the Interactions Page List

  Scenario: Go to Selectable and perform Selectable actions
    Given I navigate to Selectable link from InteractionPage
    When I perform Selectable Operations
    Then I am on Selectable page and Selectable operations are performed

  Scenario: Go to DEMO_QA site
    Given I navigate to the DEMO_QA HomePage
    When I click on Interactions
    Then I am taken to the Interactions Page List

  Scenario: Go to Resizeable and perform Resizable actions
    Given I navigate to Resizeable link from InteractionPage
    When I perform Resizeable Operations
    Then I am on Resizeable page and Resizeable operations are performed

  Scenario: Go to DEMO_QA site
    Given I navigate to the DEMO_QA HomePage
    When I click on Interactions
    Then I am taken to the Interactions Page List

  Scenario: Go to Droppable  and perform Droppable actions
    Given I navigate to Droppable link from InteractionPage
    When I perform Droppable Operations
    Then I am on Droppable page and Droppable operations are performed

  Scenario: Go to DEMO_QA site
    Given I navigate to the DEMO_QA HomePage
    When I click on Interactions
    Then I am taken to the Interactions Page List

  Scenario: Go to Draggable  and perform Draggable actions
    Given I navigate to Draggable link from InteractionPage
    When I perform Draggable Operations
    Then I am on Draggable page and Draggable operations are performed

  Scenario: Go to DEMO_QA site
    Given I navigate to the DEMO_QA HomePage

  Scenario Outline: Navigate to Widgets
    Given I click on <Operations>
    Then <Task> is Performed
    Examples:Automation Practice Switch Windows
    |       Operations           |               Task                              |
    | Widgets                    | I am taken to the Widgets Page List             |
    | Automation Practice Switch | Operations open                                 |
    | New Browser Window         | New Browser Window Operation                    |
    | New Message Window         | Open New Message Window and perform Operation   |
    | New Browser Tab            | Open New Browser Tab nd perform Operation       |
    | New DemoQA Window          | open New DemoQA Window and perform Operation    |
    | JavaScript Alert           | interact with Alert Pop-Up                      |
    | Go back to Widgets List    | I am taken to the Widgets Page List             |
    | Automation Practice Table  | Automation Table Operations Open                |
    | Table Details              | Table Details Operation                         |
    | Go back to Widgets List    | I am taken to the Widgets Page List             |
    | Automation Practice Form   | All the Automation Practice Form Operations     |
    | Go back to Widgets List    | I am taken to the Widgets Page List             |
    | Keyboard Events            | All Keyboard Events Operations                  |
    | Go back to Widgets List    | I am taken to the Widgets Page List             |
    | Tool Tip and Double Click  | All ToolTip and DoubleClick Operations          |
    | Go back to Widgets List    | I am taken to the Widgets Page List             |
    | Date Picker                | DatePicker Operation                            |
    | Go back to Widgets List    | I am taken to the Widgets Page List             |
    | Home                       | Exit The Browser                                |

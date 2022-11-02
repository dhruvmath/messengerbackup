# This is a sample Python script.
from selenium import webdriver
import selenium.webdriver.common.by

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('http://facebook.com/')
    #login
    # do it manually for now

    #Open message bubble
    # do it manually for now
    #Find Contanct
    #.find_element_by_xpath('//div[@data-testid="solid-message-bubble"]')
    #finding the MESSAGEs

    input('Waiting for you... Press enter')
    tmp = browser.find_elements('xpath', '//div[@data-scope="messages_table"]')
    print([t.text for t in tmp])

    #Save messages in a good format

    #data - testid = "message-container"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from time import sleep
from selene import have
from selene.support.shared import browser

def test_todomvc_e2e():

    browser.config.hold_browser_open = True
    # GIVEN

    browser.open('https://football.ua/')
    browser.driver.maximize_window()
    # sleep(25)
    # browser.element('div > div > div.buttons-wrapper > button.sub-dialog-btn.block_btn').click()
    browser.element('#reg-link').click()
    browser.element('#login').type('melnichukdenisss+1@gmail.com').press_enter()
    browser.element('#username').type('melnichukdenisss+1').press_enter()
    browser.element('#password1').type('password1234').press_enter()
    browser.element('#password2').type('password1234')
    sleep(10)
    browser.element('#recaptcha-anchor').click()
    sleep(10)
    browser.element('#agreement').click()
    # # THEN
    # browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    # sleep(2)
    # # WHEN
    # browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
    # sleep(2)
    # browser.element('#clear-completed').click()
    # # THEN
    # browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))
    #
    # sleep(2)

